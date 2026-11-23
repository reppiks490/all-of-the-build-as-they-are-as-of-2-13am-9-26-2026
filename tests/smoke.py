"""EPOCH Ω v3 offline Chromium regression smoke test. No provider credentials or network calls."""
from pathlib import Path
import shutil
import json, hashlib
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / 'app' / 'index.html').read_text(encoding='utf-8')
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True, executable_path=shutil.which('chromium') or None, args=['--no-sandbox', '--disable-gpu'])
    for label, width, height in [('desktop', 1440, 900), ('phone', 390, 844), ('tablet', 768, 1024)]:
        context = browser.new_context(viewport={'width': width, 'height': height}, accept_downloads=True)
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda exc: errors.append(str(exc)))
        page.set_content(HTML, wait_until='load')
        page.wait_for_timeout(100)
        assert page.locator('#spine-rows tr').count() == 8
        assert page.locator('#spine-gap').inner_text() == '$16.03'
        assert page.locator('.court-test').count() == 9
        assert page.locator('#micro-trades').inner_text() != '—'
        assert page.evaluate('portableSha256Hex("abc")') == hashlib.sha256(b'abc').hexdigest()
        page.locator('#rates').fill('200')
        page.locator('#run').click()
        page.wait_for_timeout(150)
        assert page.evaluate('window.epochV3Ready')
        page.locator('#micro-regime').select_option('panic')
        page.locator('#micro-run').click()
        first = page.locator('#micro-last').inner_text()
        page.locator('#micro-run').click()
        assert page.locator('#micro-last').inner_text() == first
        good = {
            'schema':'epoch.omega.observations.v1',
            'observations':[{'asset':'AUDIT','metric':'spot_last','source':'example','unit':'USD','value':99.5,'observedAt':'2026-11-19','capturedAt':'2026-11-23','kind':'crypto','note':'<script>malicious untrusted text</script>'}]
        }
        sample = ROOT / 'tests' / '_temporary-import.json'
        try:
            sample.write_text(json.dumps(good), encoding='utf-8')
            page.locator('#spine-upload').set_input_files(str(sample))
            page.wait_for_timeout(100)
            assert page.locator('#spine-total').inner_text() == '9'
            assert page.locator('#spine-rows script').count() == 0
            bad = {'schema': 'epoch.omega.observations.v1', 'observations': [{**good['observations'][0], 'value': 'NOT_A_NUMBER'}]}
            sample.write_text(json.dumps(bad), encoding='utf-8')
            page.locator('#spine-upload').set_input_files(str(sample))
            page.wait_for_timeout(100)
            assert 'REJECTED' in page.locator('#spine-import-status').inner_text()
            assert page.locator('#spine-total').inner_text() == '9'
            bad_date = {'schema': 'epoch.omega.observations.v1', 'observations': [{**good['observations'][0], 'observedAt': '2026-02-30'}]}
            sample.write_text(json.dumps(bad_date), encoding='utf-8')
            page.locator('#spine-upload').set_input_files(str(sample))
            page.wait_for_timeout(90)
            assert 'REJECTED' in page.locator('#spine-import-status').inner_text()
            batch = {'schema':'epoch.omega.observations.v1', 'observations': [{**good['observations'][0], 'asset':f'ATTACK{i}'} for i in range(293)]}
            sample.write_text(json.dumps(batch), encoding='utf-8')
            page.locator('#spine-upload').set_input_files(str(sample))
            page.wait_for_timeout(110)
            assert 'REJECTED' in page.locator('#spine-import-status').inner_text()
            assert page.locator('#spine-total').inner_text() == '9', 'Import must be transactional'
        finally:
            sample.unlink(missing_ok=True)
        with page.expect_download() as download_info:
            page.locator('#court-export').click()
        data = json.loads(Path(download_info.value.path()).read_text(encoding='utf-8'))
        assert data['schema'] == 'epoch.omega.evidence-passport.v3'
        assert data['fingerprint']['algorithm'] == 'SHA-256'
        assert len(data['fingerprint']['digest']) == 64
        raw = {k: v for k, v in data.items() if k != 'fingerprint'}
        assert data['fingerprint']['digest'] == hashlib.sha256(json.dumps(raw, ensure_ascii=False, separators=(',', ':')).encode('utf-8')).hexdigest()
        assert len(data['tests']) == 9
        assert not data['productionReady'] and not data['tradeExecutionEnabled']
        page.locator('#restore-evidence').click()
        assert page.locator('#spine-total').inner_text() == '8'
        assert page.evaluate('document.documentElement.scrollWidth') <= width + 2
        assert not errors, errors
        print(f'{label} {width}x{height}: PASS')
        context.close()
    browser.close()
print('ALL V3 SMOKE CHECKS PASSED')

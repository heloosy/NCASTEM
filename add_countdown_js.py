import re

js_to_add = '''
    // 5. Countdown Logic
    const targetDate = new Date('October 30, 2026 09:00:00').getTime();
    const daysEl = document.getElementById('cd-days');
    const hoursEl = document.getElementById('cd-hours');
    const minsEl = document.getElementById('cd-minutes');
    const secsEl = document.getElementById('cd-seconds');

    if(daysEl && hoursEl && minsEl && secsEl) {
        function updateCountdown() {
            const now = new Date().getTime();
            const distance = targetDate - now;

            if (distance < 0) {
                daysEl.innerText = '00';
                hoursEl.innerText = '00';
                minsEl.innerText = '00';
                secsEl.innerText = '00';
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            daysEl.innerText = days < 10 ? '0' + days : days;
            hoursEl.innerText = hours < 10 ? '0' + hours : hours;
            minsEl.innerText = minutes < 10 ? '0' + minutes : minutes;
            secsEl.innerText = seconds < 10 ? '0' + seconds : seconds;
        }

        updateCountdown();
        setInterval(updateCountdown, 1000);
    }
'''

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the closing "});" with our code + "});"
js = js.replace('});\n});', '});\n' + js_to_add + '\n});')
# wait, what if the end is just '});\n' or '});'?
# safer approach:
js = js[:-4] + js_to_add + '\n});'

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

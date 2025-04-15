function createCountdown(elementId, dates) {
    function updateCountdown() {
        const now = new Date().getTime();
        const nextDate = dates.find(date => date > now);

        if (!nextDate) {
            document.getElementById(elementId).innerHTML = "Update has dropped!";
            return;
        }

        const distance = nextDate - now;
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById(elementId).innerHTML = `
            <div><div class="countdown-frame">${formatTime(days)}</div><div class="countdown-label">Days</div></div>
            <span class="colon">:</span>
            <div><div class="countdown-frame">${formatTime(hours)}</div><div class="countdown-label">Hours</div></div>
            <span class="colon">:</span>
            <div><div class="countdown-frame">${formatTime(minutes)}</div><div class="countdown-label">Minutes</div></div>
            <span class="colon">:</span>
            <div><div class="countdown-frame">${formatTime(seconds)}</div><div class="countdown-label">Seconds</div></div>
        `;
    }

    setInterval(updateCountdown, 100);
    updateCountdown();
}

function formatTime(time) {
    return time < 10 ? `0${time}` : time;
}

// const currentYear = new Date().getFullYear();

// createCountdown("countdown", [
//     new Date(`March 14, ${currentYear} 12:00:00`).getTime()
//     // new Date(`March 8, ${currentYear} 17:52 :00`).getTime()
// ]);

// function displayNew(){

// }

// function wait(releaseTime) {
//     var interval = setInterval(() => {
//         var now = new Date().getTime();
//         const distance = releaseTime - now;

//         if (distance <= 0) {
//             clearInterval(interval);
//         }
//     }, 1000);
// }

// // Example usage: Wait until a specific date and time
// let targetDate = new Date("March 10, 2025 15:30:00").getTime();
// wait(targetDate);
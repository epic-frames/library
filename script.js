const version = "webv1.0.832"

const main_news = [
    {
        id: 7,
        release: "8 May, 2025 16:00:00",
        title: 'Upcoming Update Detailed Brakedown',
        date: "8 May, 2025",
        content: 'This is the deatiled bakedown of the update coming this friday with deatiled explanations for each of the features added. The article is accessible <a style="color: gray;" href="https://drive.google.com/file/d/1DM0ftl7v5doEDUSu36giyuZLDLcQtYTK/view?usp=sharing">here</a>.',
        image: "Assets/health_sneak_peak.png"
    },
    {
        id: 6,
        release: "11 April, 2025 16:00:00",
        title: 'New Version of "Cave of Malice" (still in beta-development)',
        date: "11 April, 2025",
        content: 'A new version of "Cave of Malice" has just dropped with coins and a shop. Check out the game versions for more detail',
        image: "Assets/COM.png"
    },
    {
        id: 3,
        release: "10 March, 2025 19:12:30",
        title: 'Open Beta-testing for "Cave Of Mailce"',
        date: "20 February, 2025",
        content: '"Cave of Malice" is now available for worldwide beta testing on our website until version 1.0.0 is released. Please be aware that this is a beta version and may contain some bugs. If you come across any issues, please report them to epicframe.email@gmail.com.',
        image: "Assets/COM.png"
    },
    {
        id: 1,
        release: "1 January, 2025 00:00:00",
        title: 'Development of "Asteroid Avoider 3000"',
        date: "17 January, 2025",
        content: "With the latest update (v1.3), we are stopping further development of this game, but something interesting is coming soon.",
        image: "Assets/photo-1.png"
    }
];

const news = [
    {
        id: 7,
        show: true,
        release: "8 May, 2025 16:00:00",
        tags: "New Update Brakedown",
        title: 'Upcoming Update Detailed Brakedown',
        date: "8 May, 2025",
        content: 'This is the deatiled bakedown of the update coming this friday with deatiled explanations for each of the features added. The article is accessible <a style="color: gray;" href="https://drive.google.com/file/d/1DM0ftl7v5doEDUSu36giyuZLDLcQtYTK/view?usp=sharing">here</a>.',
        image: "Assets/health_sneak_peak.png"
    },
    {
        id: 6,
        show: true,
        release: "11 April, 2025 16:00:00",
        tags: "New Update",
        title: 'New Version of "Cave of Malice" (still in beta-development)',
        date: "11 April, 2025",
        content: 'A new version of "Cave of Malice" has just dropped with coins and a shop. Check out the game versions for more detail',
        image: "Assets/COM.png"
    },
    {
        id: 5,
        show: true,
        release: "21 March, 2025 10:00:00",
        tags: "Emergency Update",
        title: 'Emergency update for "Cave of Malice"',
        date: "21 March, 2025",
        content: 'Because of some errors on our side we will be releasing a new patch update for the recent update: v0.2.1. We will also be adding a new freeze bg as a thank you for you waiting.',
        image: "Assets/freeze_bg.png"
    },
    {
        id: 4,
        show: true,
        release: "20 March, 2025 16:00:00",
        tags: "News",
        title: 'New version for "Cave of Malice"',
        date: "20 March, 2025",
        content: 'A new versions has come with 2 new levels and a new cave creature',
        image: "Assets/COM.png"
    },
    {
        id: 3,
        show: true,
        release: "1 January, 2025 00:00:00",
        tags: "News",
        title: 'Open Beta-testing for "Cave Of Mailce"',
        date: "20 February, 2025",
        content: '"Cave of Malice" is now available for worldwide beta testing on our website until version 1.0.0 is released. Please be aware that this is a beta version and may contain some bugs. If you come across any issues, please report them to epicframe.email@gmail.com.',
        image: "Assets/COM.png"
    },
    {
        id: 2,
        show: true,
        release: "1 January, 2025 00:00:00",
        tags: "News",
        title: "New Game Release",
        date: "15 February, 2025",
        content: 'Epic Frame Studios is happy to announce that we are starting the development of a brand new game called "Cave of Malice". This game is a platformer game where you have to jump on platforms to get through and move on to the next level. We will update you as time goes by. Note: The photo above is only our inspiration.',
        image: "Assets/photo-2.jpg"
    },
    {
        id: 1,
        show: true,
        release: "1 January, 2025 00:00:00",
        tags: "News",
        title: 'Development of "Asteroid Avoider 3000"',
        date: "17 January, 2025",
        content: "With the latest update (v1.3), we are stopping further development of this game, but something interesting is coming soon.",
        image: "Assets/photo-1.png"
    }
];


const sp = [
    {
        id: 1,
        show: false,
        release: "8 April, 2025 17:00:00",
        content: `
        <div class="sp-content">
            <h3 class="text-xl font-semibold">Something big is coming!</h3>
            <p class="sp-date">8 April, 2025</p>
            <p class="sp-text">A ability will be added in the next update that might change your entire playstyle!</p>
            <img src="Assets/sneak_peak.png" alt="A new creature!" class="sp-image">
        </div>
        `
    },
    {
        id: 2,
        show: false,
        release: "7 May, 2025 17:00:00",
        content: `
        <div class="sp-content">
            <h3 class="text-xl font-semibold">The second update for the shop is here this Friday!</h3>
            <p class="sp-date">7 May, 2025</p>
            <p class="sp-text">In this update we redesigned the shop to help improve the playing experience</p>
            <img src="Assets/health_sneak_peak.png" alt="New Health System" class="sp-image">
        </div>
        `
    }
];


const games = [
    {
        id: 2,
        title: "Cave of Malice",
        dtitle: "cave_of_malice",
        description: "A platformer set in a cave with cave creatures.",
        image: "Assets/COM-N.png",
        versions: [
            { version: "v0.4.0", date: "9 May, 2025", notes: "Completed the shop with a new wheel to spin and more upgrades"},
            { version: "v0.3.0", date: "11 April, 2025", notes: "Added a new shop where you can buy upgrades with coins"},
            { version: "v0.2.1", date: "21 March, 2025", notes: "This is a emergency update with some new feature based on the version 0.2.0"},
            // { version: "v0.1.0", date: "20 February, 2025", notes: "Initial launch (open beta testing)"}
        ]
    },
    {
        id: 1,
        title: "Asteroid Avoider 3000",
        dtitle: "asteroid_avoider",
        description: "A game where you have to avoid asteroids.",
        image: "Assets/AA3000.png",
        versions: [
            { version: "v1.3.0", date: "17 January, 2025", notes: "Added a new settings page"},
            { version: "v1.2.0", date: "9 January, 2025", notes: "New sprite and music"}
        ]
    }
];

const versions = {
    "Asteroid_Avoider_3000": [
        {
            id: 4,
            name: "1.3.0",
            description: `Update Content: <br>
                            - Added a settings page: <br>
    &nbsp;&nbsp;&nbsp;&nbsp;    - Added the ability to change the music volume <br>
    &nbsp;&nbsp;&nbsp;&nbsp;    - Added a key tutorial to play the game <br>
                            - Added a new player sprite <br>
                            - Added a local high-score leaderboard <br>
                            - Minor file optimisations`,
            date: "17 January, 2025",
            size: "7.1MB"
        },
        {
            id: 3,
            name: "1.2.0",
            description: `Update Content:
                            - Added a new sloweroid sprite <br>
                            - Added game music for the start menu <br>
                            - Added game optimizations <br>
                            - Enhanced the debugging mode (You can now enter debug mode by pressing 1) <br>
                            - Made sloweroid bigger to provide more challenge <br>
                            - Adjusted the sloweroid falling speed`,
            date: "9 January, 2025",
            size: "7.1MB"
        },
        {
            id: 2,
            name: "1.1.0",
            description: `Update Content: <br>
                            - Added a startup animation <br>
                            - Added different chances for different types of asteroids for each difficulty level <br>
                            - Added a debug mode <br>
                            - Fixed minor bugs`,
            date: "26 December, 2024",
            size: "98KB"
        },
        {
            id: 1,
            name: "1.0.0",
            description: "Initial launch",
            date: "20 December, 2024",
            size: "98KB"
        }
    ],
    "Cave_Of_Malice": [
        {
            id: 5,
            name: "0.4.0",
            description: "The May Drop comes with changes to the games economy and the shop. The last update before v1.0.0",
            date: "9 May, 2025",
            size: "61.7MB"
        },
        {
            id: 4,
            name: "0.3.0",
            description: "The April Drop has just been released where you can access our brand new menu with upgrades you can buy for the new coins which have also been added in this recent update. Coins are found on all the levels (usually 3 - 4 coins per level). You can use these coins to upgrade your player's stats. Note: The coin economy is still in development and a lot of things are subject to change.",
            date: "11 April, 2025",
            size: "61.7MB"
        },
        {
            id: 3,
            name: "0.2.1",
            description: "This is a emergency update with some new feature based on the version 0.2.0.",
            date: "21 March, 2025",
            size: "30.8MB"
        },
        {
            id: 2,
            name: "0.2.0",
            description: "In this update, we added 2 new levels (level 2 and level 3), a new enemy (The Watcher) and minor bug fixes.",
            date: "20 March, 2025",
            size: "15.4MB"
        },
        {
            id: 1,
            name: "0.1.0",
            description: "Initial launch in open beta testing. Note: This version will be discontinued after v1.0.0.",
            date: "20 February, 2025",
            size: "71KB"
        }
    ]
}

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

    setInterval(updateCountdown, 1000);
}

function formatTime(time) {
    return time < 10 ? `0${time}` : time;
}


function renderMainNews() {
    try {
        const newsContainer = document.getElementById('newsContainer');
        newsContainer.innerHTML = main_news.filter(item => new Date(item.release).getTime() <= new Date().getTime()).map(item => `
            <div class="news-card">
                <img src="${item.image}" alt="${item.title}" class="news-image">
                <div class="news-content">
                    <h3 class="text-xl font-semibold">${item.title}</h3>
                    <p class="news-date">${item.date}</p>
                    <p>${item.content}</p>
                </div>
            </div>
        `).join('');
    } catch (TypeError) {}
}


function renderNews() {
    try {
        const newsContainer = document.getElementById('newsContainer');
        newsContainer.innerHTML = news.filter(item => item.show === true && new Date(item.release).getTime() <= new Date().getTime()).map(item => `
            <div class="news-card">
                <img src="${item.image}" alt="${item.title}" class="news-image">
                <div class="news-content">
                    <h3 class="text-xl font-semibold">${item.title}</h3>
                    <p style="color: #9ca3af; font-size: 0.875rem;">Tags: ${item.tags}</p>
                    <p class="news-date">${item.date}</p>
                    <p>${item.content}</p>
                </div>
            </div>
        `).join('')
    } catch (TypeError) {}
}


function renderSneakPeeks() {
    try {
        const spSection = document.getElementById('sneakPeekSection');
        spSection.outerHTML = `
        <section class="section" id="sneakPeekSection">
            <h2 class="section-header"><span class="icon">👀</span> Sneak Peeks</h2>
            <div id="sneakPeekContainer" class="news-grid"></div>
        </section>
            `
        const spContainer = document.getElementById('sneakPeekContainer');
        spContainer.innerHTML = sp.filter(sp => sp.show === true && new Date(sp.release).getTime() <= new Date().getTime()).map(sp => `
            <div class="news-card">
                ${sp.content}
            </div>
        `).join('')
    } catch (TypeError) {}
}

function renderGames() {
    try {
        const gamesContainer = document.getElementById('gamesContainer');
        gamesContainer.innerHTML = games.map(game => `
            <div class="game-card">
                <div class="game-image-container">
                    <img src="${game.image}" alt="${game.title}" class="game-image">
                </div>
                <div class="game-details">
                    <h3 class="text-2xl font-bold mb-4">${game.title}</h3>
                    <p class="text-gray-300 mb-6">${game.description}</p><br>
                    <a class="downloads" href="${game.dtitle}.html">Browse versions</a>
    
                    <div class="version-history">
                        <h4 class="text-lg font-semibold mb-4">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"
                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" class="icon" style="display: inline; margin-right: 0.5rem;">
                                <circle cx="12" cy="12" r="10"></circle>
                                <polyline points="12 6 12 12 16 14"></polyline>
                            </svg>
                            Version History
                        </h4>
                        ${game.versions.map(v => `
                            <div class="version-card">
                                <div class="version-header">
                                    <span class="font-semibold">${v.version}</span>
                                    <span class="text-sm">${v.date}</span>
                                </div>
                                <p class="text-gray-300">${v.notes}</p>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        `).join('');
    } catch (TypeError) {}
}


function renderVersions(gameName) {
    const versionsContainer = document.getElementById('versionsContainer');

    if (!versions[gameName] || versions[gameName].length === 0) {
        versionsContainer.innerHTML = "<p>No versions available for this game.</p>";
        return;
    }

    versionsContainer.innerHTML = versions[gameName].map(version => `
        <div class="version-card">
            <h3>Version ${version.name}</h3>
            <p>${version.description}</p>
            <div class="version-info">
                <p><strong>Release Date:</strong> ${version.date}</p>
                <p><strong>Size:</strong> ${version.size}</p>
            </div>
            <button class="download-btn" onclick="downloadVersion('${gameName}', '${version.name}')">
                Download Version ${version.name}
            </button>
        </div>
    `).join('');
}

function renderFooter() {
    const footer = document.getElementById('footer');
    footer.innerHTML = `
        <p>2025 Epic Frame Studio</p>
        <p style="font-size: 0.9rem;">Running ${version}</p>
        `
}


function downloadVersion(game, version) {
    a = `Versions/${game}/${game}_v${version}.zip`
    window.location.href = a
    alert(`Downloading version ${version}...`);
}

function render(){
    if (sp.length > 0 & sp.some(item => item.show && new Date(item.release).getTime() <= new Date().getTime())) {
        renderSneakPeeks();
    }
    // if (news.length > 0 & news.some(item => item.show && new Date(item.release).getTime() <= new Date().getTime())) {
    //     renderNews();
    // }
    // if (main_news.length > 0 & main_news.some(item => item.show && new Date(item.release).getTime() <= new Date().getTime())) {
    //     renderMainNews();
    // }
}

// Initial render
renderFooter();
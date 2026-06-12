fetch('./matches.json')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('matches-container');
        container.innerHTML = ''; 

        data.forEach(day => {
            const dayTitle = document.createElement('h3');
            dayTitle.innerText = day.date;
            container.appendChild(dayTitle);

            day.matches.forEach(match => {
                const matchDiv = document.createElement('div');
                matchDiv.className = 'match-card';
                
                // هنا الجزء السحري: ننشئ الرابط بشكل صحيح
                matchDiv.innerHTML = `
                    <p>${match.home} ضد ${match.away} - ${match.time}</p>
                    <a href="${match.link}" target="_blank" style="padding: 10px; background: blue; color: white; text-decoration: none; border-radius: 5px;">
                        مشاهدة المباراة
                    </a>
                    <hr>
                `;
                container.appendChild(matchDiv);
            });
        });
    })
    .catch(error => console.error('خطأ في تحميل البيانات:', error));

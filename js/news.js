// 
// Author: Vikas Kumar (@dzenvikas)
// 

country_code = 'us';

var url = 'https://newsapi.org/v2/top-headlines?' +
    'country=' + country_code + '&' +
    'apiKey=6e214863d0dc494fb5cd74b4d29ac4ff';

var req = new Request(url);

fetch(req)
    .then(response => response.json())
        .then(result => {
            i = 1;
            total_div = 8
            while (i <= (total_div)) {
                image = result['articles'][i-1]['urlToImage'];
                title = result['articles'][i-1]['title'];
                desc = result['articles'][i-1]['description'];
                source = result['articles'][i-1]['source']['name'];

                myURL = 'url(' + image + ')';    //url(link)
                // console.log(typeof image);
                document.getElementById('card__image-' + i).style.backgroundImage = myURL;

                document.getElementById('card__title-' + i).innerHTML = title + ' ...';
                
                document.getElementById('card__desc-' + i).innerHTML = desc + ' ...';
                
                document.getElementById('card__source-' + i).innerHTML = source;

                i+=1;
            };
        })



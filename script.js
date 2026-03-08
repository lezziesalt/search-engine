const pages = [
{
title: "OpenAI",
url: "https://openai.com",
description: "Artificial intelligence research lab"
},

{
title: "GitHub",
url: "https://github.com",
description: "Code hosting platform"
},

{
title: "Wikipedia",
url: "https://wikipedia.org",
description: "Free online encyclopedia"
}
];

function search(){

let query = document.getElementById("searchBox").value.toLowerCase();
let results = document.getElementById("results");

results.innerHTML = "";

pages.forEach(page => {

if(page.title.toLowerCase().includes(query) ||
page.description.toLowerCase().includes(query)){

results.innerHTML += `
<div class="result">
<h3><a href="${page.url}" target="_blank">${page.title}</a></h3>
<p>${page.description}</p>
</div>
`;

}

});

}

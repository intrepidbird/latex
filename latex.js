$(document).ready(function() {
    $('#latexForm').submit(function(e) {
        e.preventDefault();
        let latexCode = $('#latexCode').val();
        let imageUrl = 'https://latex.codecogs.com/svg.latex?' + encodeURIComponent(latexCode);
        let imageHtml = '<img src="' + imageUrl + '" class="latex-image">';
        $('#latexOutput').html(imageHtml);
    });
});


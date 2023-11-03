$(document).ready(function() {
    $('#latexGeneratorForm').submit(function(e) {
        e.preventDefault();
        let equation = $('#equation').val();
        let latexOutput = generateLatex(equation);
        $('#latexOutput').val(latexOutput);
    });

    function generateLatex(equation) {
        // Logic to generate Latex from equation
        // Replace this with your own logic
        let latex = "\\[ " + equation + " \\]";
        return latex;
    }
});

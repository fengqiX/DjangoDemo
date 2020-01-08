
$(document).ready(function(){

    $(".comment a").on('click', (evt) => {
//    alert("yes")
        evt.preventDefault()
        let anchor = $(evt.target)
        let url = anchor.attr('href')
        $.getJSON(url, (json) => {
            if (json.code == 200) {
                let span = anchor.next()
                span.text(parseInt(span.text()) + 1)
            } else {
                alert(json.hint)
            }
        })
    })

});
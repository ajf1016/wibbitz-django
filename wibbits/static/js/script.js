$(document).ready(function() {
    $(document).on('submit', 'form.ajax',function(e){
        e.preventDefault();
        var $this = $(this);

        var url = $this.attr("action")
        var method = $this.attr("method")

        jQuery.ajax({
            type: method,
            url: url,
            dataType: "json",
            data :new FormData(this),
            processData: false,
            contentType: false,
            cache: false,
            success: function(data){
                console.log(data);

                var title = data["title"];
                var text = data["message"];
                var status = data["status"];

                Swal.fire({
                    icon : status,
                    title : title,
                    text : text,
                });
                if(status == "success"){
                    $this.trigger("reset");
                }
            },
            error : function(error){
                console.log(error)
            }
        })
    })
})
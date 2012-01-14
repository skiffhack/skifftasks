/*
// custom js, e.g.
Tasket.settings.USERS_CAN_CREATE_HUBS = false;

app.bind("ready", function () {
alert("Tasket boilerplate custom code")
});
*/

$(document).ready(function(){
  jQuery('a[href="#/sign-up/"]').remove();
  jQuery('a[href="#/account/"]').attr("href","");
  
  jQuery('#browserid').bind('click', function(e) {
    e.preventDefault();
    navigator.id.getVerifiedEmail(function(assertion) {
      if (assertion) {
       jQuery.ajax({
          url: "/browserid/verify/",
          type: "POST",
          contentType: "application/json",
          // TODO: this should use JSON.stringify in case password contains double-quotes
          data: assertion,
          success: function (data) {
            var user = new User(data.user);
            app.updateCurrentUser(user);
            app.lightbox.hide();
            if (app.notification){
                app.notification.success("You are now logged in.");
            }
          }
        });
      }
    });
  });
});

let email = document.getElementById("email");
        let pass = document.getElementById("password");
        email.onfocus = function(){EmailFocus()};
        email.onblur = function(){EmailBlur()};
        pass.onfocus = function(){PassFocus()};
        pass.onblur = function(){PassBlur()};

        function EmailFocus() {
            email.style.border = "5px DodgerBlue solid";
        }

        function EmailBlur() {
            email.style.border = "1px gray solid";
        }

        function PassFocus() {
            pass.style.border = "5px DodgerBlue solid";
        }

        function PassBlur() {
            pass.style.border = "1px gray solid";
        }
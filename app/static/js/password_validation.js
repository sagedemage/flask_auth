class Switch {
    /* Class for turning on or off the switch */
    switch_status = 0;

    constructor() {
    }

    set_switch(value) {
        /* set the switch state */
        this.switch_status = value;
    }

    get_switch() {
        /* get the switch state */
        return this.switch_status;
    }
}

let passwordField = document.getElementById("password");
let letter = document.getElementById("letter");
let lowerCase = new Switch();
let upperCase = new Switch();
let num = new Switch();
let progress_bar = document.getElementById("p-bar");

function ModifyProgressBar(current_width) {
    /* Increase or Decrease the progress bar */
    let width_string_new_value = current_width.toString();
    let new_width_value = width_string_new_value.concat("%");
    progress_bar.style.width = new_width_value;
}

function IncreaseProgressBarOnce(switch_object, inc_value, width_current_value) {
    /* Increase progress bar if the password condition is met */
    if (switch_object.get_switch() === 0) {
        width_current_value += inc_value;
        switch_object.set_switch(1);
    }
    return width_current_value;
}

function DecreaseProgressBarOnce(switch_object, inc_value, width_current_value) {
    /* Decrease progress bar after removing the character that meet the condition */
    if (switch_object.get_switch() === 1) {
        width_current_value -= inc_value;
        switch_object.set_switch(0);
    }
    return width_current_value;
}

passwordField.onfocus = function () {
    /* Add effect on the password field when it is on focus */
    let message = document.getElementById("message");
    message.style.display = "block";
    message.style.border = "1px solid";
}

passwordField.onkeyup = function () {
    /* Validate the password on key up */
    // Validate lowercase letters
    let lowerCaseLetters = /[a-z]/g;
    let upperCaseLetters = /[A-Z]/g;
    let numbers = /[0-9]/g
    let p_bar_width_string = progress_bar.style.width;
    let width_current_value = parseInt(p_bar_width_string.substring(0, p_bar_width_string.length - 1));

    // Increase the progress bar if there is a lowercase letter
    if (passwordField.value.match(lowerCaseLetters)) {
        width_current_value = IncreaseProgressBarOnce(lowerCase, 33, width_current_value);
        ModifyProgressBar(width_current_value);
    }
    // Decrease the progress bar if there is no lowercase letter
    else {
        width_current_value = DecreaseProgressBarOnce(lowerCase, 33, width_current_value);
        ModifyProgressBar(width_current_value);
    }

    // Increase the progress bar if there is an uppercase letter
    if (passwordField.value.match(upperCaseLetters)) {
        width_current_value = IncreaseProgressBarOnce(upperCase, 33, width_current_value);
        ModifyProgressBar(width_current_value);
    }
    // Decrease the progress bar if there is no uppercase letter
    else {
        width_current_value = DecreaseProgressBarOnce(upperCase, 33, width_current_value);
        ModifyProgressBar(width_current_value);
    }

    // Increase the progress bar if there is a number
    if (passwordField.value.match(numbers)) {
        width_current_value = IncreaseProgressBarOnce(num, 34, width_current_value);
        ModifyProgressBar(width_current_value);
    }
    // Decrease the progress bar if there is no number
    else {
        width_current_value = DecreaseProgressBarOnce(num, 34, width_current_value);
        ModifyProgressBar(width_current_value);
    }
}
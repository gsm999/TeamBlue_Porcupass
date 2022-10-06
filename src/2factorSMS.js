import {
    multiFactor, PhoneAuthProvider, PhoneMultiFactorGenerator,
    RecaptchaVerifier
} from "firebase/auth";

const recaptchaVerifier = new RecaptchaVerifier("sign-in-button", {
    "size": "invisible",
    "callback": function (response) {
        // reCAPTCHA solved, you can proceed with
        // phoneAuthProvider.verifyPhoneNumber(...).
        onSolvedRecaptcha();
    }
}, auth);
multiFactor(user).getSession()
    .then(function (multiFactorSession) {
        var phoneNumber = prompt("Please enter your phone number.")
        const phoneInfoOptions = {
            phoneNumber: phoneNumber,
            session: multiFactorSession
        };

        const phoneAuthProvider = new PhoneAuthProvider(auth);

        // Send SMS verification code.
        return phoneAuthProvider.verifyPhoneNumber(phoneInfoOptions, recaptchaVerifier);
    }).then(function (verificationId) {
        // Ask user for the verification code. Then:
        const cred = PhoneAuthProvider.credential(verificationId, verificationCode);
        const multiFactorAssertion = PhoneMultiFactorGenerator.assertion(cred);

        // Complete enrollment.
        return multiFactor(user).enroll(multiFactorAssertion, mfaDisplayName);
    });
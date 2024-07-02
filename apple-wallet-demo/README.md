# What you need to create pkpass

## When Creating Account For New Client

### Pass Type ID
Create the Pass Type ID with the apple developer account
keep the identifier you decided to use (`pass.XXX`)
identifier: "pass.for.wallet.app.pkpass.in.code"

### Pass Type ID Certificate
Create the Pass Type ID Certificate with the apple developer account

After creating the Pass Type ID and Certificate, download the certificate to your computer

### Export the certificate you downloaded to .p12 file
Use the Keychain tool in Mac in order to export the certificate to .p12 - `Certificates.p12`


### Create key and certificate out of the .p12 file
#### creating the certificate:
`openssl pkcs12 -in Certificates.p12 -clcerts -nokeys -out passcertificate.pem -passin pass:<import password>`

#### creating the key:
`openssl pkcs12 -in Certificates.p12 -nocerts -out passkey.pem -passin pass:<import password> -passout pass:<key password>`


## From this step on, this should run when creating the pkpass

### create a manifest.json
you can use the [generate_manifest.py](generate_manifest.py) script

### create a signature file:
`openssl smime -binary -sign -certfile WWDR.pem -signer passcertificate.pem -inkey passkey.pem -in manifest.json -out signature -outform DER -passin pass:<key password>`

#### pay attention that you have the `<key password>` from "creating the key" step


### create the zip file
for example:

`zip -r <wallet pass name>.pkpass manifest.json pass.json signature icon.png thumbnail@2x.png icon@2x.png logo.png logo@2x.png thumbnail.png`

### convert the zip to pkpass
Just change the extension file name from `.zip` to `.pkpass`







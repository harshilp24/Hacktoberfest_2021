// this programms provides an access to a site through login and password. If the password and login are correct, the access if available. If not, the access is not available
const UsLog = 'Balka123';
const UsPas = 'master31';
const rUsLog = 'Balka123';
const rUsPas = 'master321';

if(UsLog==rUsLog && UsPas==rUsPas) {
    console.log ('Access is available');
}
else {console.log ('Access is not avilable')}
if(UsLog!=rUsLog) {
    console.log ('Wrong Login')
}
if (UsPas!=rUsPas) {
    console.log ('Wrong Password')
}

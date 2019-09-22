let ip = "localhost:5000";

function wait(ms) {
    var start = Date.now(),
        now = start;
    while (now - start < ms) {
      now = Date.now();
    }
}

let load = `

<img src="https://thumbs.gfycat.com/ObviousQuarrelsomeIntermediateegret-max-1mb.gif" align="center" style="margin-left: 42.5%; margin-top: 12%; height: 200px; width: 200px;">
    
&nbsp;&nbsp;<p class="h3-h" align="center">LOADING...</p>



`;

let newDOM = `

<!-- ################################################################################################# -->
        <div class="headerBar">
                <div class="user-photo"><img src="Images/face.png"></div>
                <p class="title">Ana Datanautix</p>
                
                <button id="exit"><img src="last.ico" style="height: 40px; width:40px; margin-left: 200%; margin-top: 24%; opacity: 0.8;"></button>
        </div>
        
        
        <!-- ################################################################################################# -->
        <div class="chatbox">

            <div class="chatlogs" id="chatArea">
            
                <div class="chat friend">
                    <div class="user-photo"><img src="Images/face.png"></div>
                    <p class="chat-message">Hello, ask me anything!</p>
                </div>



                <div class="chat friend" id="loadingGif" style="display: none;">
                    <div class="user-photo"><img src="Images/face.png"></div>
                    <div class="gif"><img src="Images/loading.gif"></div>
                </div>

            </div>            
        </div>
        

        <!-- ################################################################################################# -->
        <div class="chat-form">
            
            <div id="inputDiv">
                <div id="buttonDiv"></div>
                <textarea id="msg_inp" class="input" placeholder="Message" rows="1" data-min-rows='1'></textarea>
            </div>
            
            <div id="chat-form-buttons">
                <input type ="image"id="mike" src="Images/microphone.png">
            </div>

            <div id="chat-form-buttons">
                <input type ="image" id="rec" src="Images/send_icon.png">
            </div>

        </div>
        
      </div>
    </div>
        <!-- ################################################################################################# -->

    
	

        
`;


function Autocomplete(){
    var questions = ["What are the advantages of HPE OneView",
                "What is a software-defined approach to lifecycle management",
                "Can I customize functionality and integrate HPE OneView with my existing tools and environment",
                "Does HPE provide integration kits for customers who do not wish to develop their own",
                "Is HPE OneView a refresh to existing HPE infrastructure management tools or a brand-new design",
                "What capabilities does HPE OneView offer",
                "How is HPE OneView licensed",
                "What server platforms are supported by HPE OneView 5.0",
                "Can I create a template from an existing profile",
                "Does HPE OneView support granular access control",
                "What is two-factor authentication and is it supported by HPE OneView",
                "What is an SPP",
                "Does HPE OneView use SPPs to update the firmware and driver of servers",
                "Does HPE OneView support external repository to store SPPs",
                "Can you schedule the activation of firmware and OS driver updates",
                "Does HPE OneView allow online profile configuration changes",
                "What tools HPE OneView use for Firmware and Driver updates",
                "How does HPE OneView handle Firmware and Driver updates",
                "Does HPE OneView support configuration of iLO settings",
                "What are the latest enhancements with HPE OneView Remote support",
                "What kind of cluster profile support is offered by HPE OneView",
                "Can I view DIMM inventory with HPE OneView",
                "Does HPE OneView support IPv6",
                "Does HPE OneView provide firmware compliance checking:",
                "Does HPE OneView support HPE 3PAR StoreServ",
                "Does HPE OneView support HPE Nimble Storage",
                "If Flat SAN is used, can you see FC bandwidth usage data",
                "What is the HPE OneView support for Brocade FC ICM",
                "What can I use for Brocade SAN automated zoning with BNA support going away",
                "Does HPE OneView support automated volume provisioning",
                "Does HPE OneView support HPE StoreVirtual 3200 series",
                "Does HPE OneView support StoreVirtual managed nodes",
                "Does HPE OneView support automated SAN Storage volume provisioning for DL/Apollo Servers",
                "Does HPE OneView support Brocade SAN storage",
                "Can I do a migration from the Virtual Connect Manager to an HPE OneView environment without the need to power off servers",
                "How many FlexNIC/FlexHBA per port does the FlexFabric support in HPE OneView",
                "What is the integration with the IMC tool",
                "Does HPE OneView support the B22HP FEX interconnect modules",
                "Does HPE OneView support the LACP on s-channels",
                "What is an Active/Active configuration",
                "How does HPE OneView work with HPE switches,What can be done today in terms of management and configuration",
                "Can HPE OneView manage the external top-of-rack Cisco (ToR) switch",
                "Can HPE OneView manage the external top-of-rack Arista (ToR) switch",
                "What is HPE Composable Ecosystem Program",
                "What Microsoft plug-ins are in the HPE OneView Advanced 5.0 release",
                "What VMware plug-ins are in the HPE OneView Advanced 5.0 release",
                "How are the partner integrations licensed for VMware and Microsoft",
                "How is HPE OneView delivered",
                "Does HPE OneView replace the need for HPE Systems Insight Manager, HPE Insight Control, and HPE Virtual Connect Enterprise Manager",
                "How long will Hewlett Packard Enterprise support the current HPE SIM, product",
                "Are license upgrades available from Insight Management software to HPE OneView Advanced",
                "What support and services are available for HPE OneView",
                "How do I get training on HPE OneView",
                "Can a user access inventory and health status information consolidated by HPE OneView Global Dashboard using an API",
                "How does HPE OneView Global Dashboard help customers manage at scale",
                "What systems does HPE Global Dashboard support",
                "How is HPE OneView Global Dashboard delivered",
                "Can I schedule an HPE OneView Global Dashboard report",
                "How can I track the assignment of HPE OneView licensed across my data centers",
                "Does HPE OneView Global Dashboard support IPv6",
                "Does HPE OneView Global Dashboard support interconnect modules",
                "Does HPE OneView Global Dashboard display remote support status",
                "Does Remote Technician require Remote Support",
                "Is there a charge for Remote Technician",
                "Is a support case required for Remote Technician",
                "Do I need to add firewall rules",
                "Can I time-box access , Does it time out",
                "Will the access be tracked and audited—what somebody did to what resource at what time",
                "Will keystrokes be captured",
                "What is the benefit of this versus using HPE MyRoom for screen sharing",
                "Does Remote Technician make it easier to provide support dumps and logs",
                "Is this technology unique to HPE OneView—how mature is it,How many people are using it",
                "Will Remote Technician be available for Image Streamer",
                "Is there a terminate remote technician if something is amiss"];
                $( "#msg_inp" ).autocomplete({  
                    source: questions,
                    position: {
                        my: "left top",
                        at: "left bottom",
                        collision: "flip"
                        },
                    minlength: 3,
                    collision: "fit"
                });  
}

// Function for Logging in
function Login (name, pass) {
    var arr = {'username':name, 'password': pass};
    loading();
    $.ajax(
        {
                url: "http://" + ip + "/signin",
                type: "POST",
                data: JSON.stringify(arr),
                contentType: 'application/json;charset=UTF-8',
                success: function(res) {
                    
                    console.log(res);
                    if(res.data){
                        localStorage.token = res.data.token;
                    console.log('Got a token from the server! Token: ' + localStorage.token);
                    localStorage.userid = res.data.id;
                    localStorage.name = res.data.username; 
                    
                    console.log(localStorage.userid + " " + localStorage.name);
                    chat(localStorage.userid);
                    }
                    
                    wait(2000);
                    if(res.data){
                        let dom = document.querySelector(".container_new");
                        dom.remove();
                                

                        let new_dom = document.createElement("div");
                        let a_atr = document.createAttribute("class");
                        a_atr.value = "container";
                        new_dom.setAttributeNode(a_atr);

                        new_dom.innerHTML = newDOM;
                        document.body.appendChild(new_dom);
                        //document.body.appendChild(recording);
                        btn = document.getElementById("rec");
                        msg = document.getElementById("msg_inp");
                        exit = document.getElementById("exit");
                        btn.addEventListener("click", function(){
                            let text = msg.value;
                            send(text);
                            msg.value = "";
                        });
                        $('#msg_inp').keypress(function(event){
                            var keycode = (event.keyCode ? event.keyCode : event.which);
                            if(keycode == '13'){
                                let text = msg.value;
                                send(text);
                                msg.value = ""; 
                            }
                        });
                        exit.addEventListener("click",function(){
                            Logout();
                        })
                        window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
                        let finalTranscript = '';
                        let recognition = new window.SpeechRecognition();
                        recognition.interimResults = true;
                        recognition.maxAlternatives = 10;
                        recognition.continuous = false;
                        recognition.onresult = (event) => {
                        let interimTranscript = '';
                        for (let i = event.resultIndex, len = event.results.length; i < len; i++) {
                                let transcript = event.results[i][0].transcript;
                                if (event.results[i].isFinal) {
                                finalTranscript = transcript;
                                } else {
                                interimTranscript = transcript;
                                }
                            }
                            msg.value = "";
                            msg.value = finalTranscript;
                        }
                    
                        mike.addEventListener("click",function(){
                            recognition.start();
                        })

                        // Autocomplete
                        Autocomplete();



                    }
                    else{
                        Logout();
                        wait(3000);
                        console.log("Login Failed")
                        alert("Login Failed");
                    }
                                    
                },
                error: function() {
                    Logout();
                    wait(3000);
                    console.log("Login Failed")
                    alert("Login Failed");
                    
                }
            }
    );
}




function loading(){

    document.querySelector(".container_new").remove();
    console.log("Removed");
    let dd = document.createElement("div");
    let dd_atr = document.createAttribute("class");
    dd_atr.value = "container_new";
    dd.setAttributeNode(dd_atr);

    dd.innerHTML = load;
    
    document.body.appendChild(dd);
    console.log("Child Added");  
    // wait(5000);
    console.log("Loaded ** * ");
                                    
}


// Function for Logging out
function Logout(){
    localStorage.clear();
    window.location.replace("");

}





// Function for Registration
function Register (name, pass) {

    var arr = {'username':name, 'password': pass};
    $.ajax(
        {
            url: "http://" + ip + "/signup",
            type: "POST",
            data: JSON.stringify(arr),
            contentType: 'application/json;charset=UTF-8',
            success: function(data) {
                console.log(data);
                alert("Successful Signup...")
            },
            error: function() {
                alert("Registration Failed");
            }
        }
    );
}





// Function for Chatting initiation
function chat(userid){

    let arr = {'user': userid};
    $.ajax(
        {
            url: "http://" + ip + "/chat",
            type: "POST",
            data: JSON.stringify(arr),
            contentType: 'application/json;charset=UTF-8',
            beforeSend: function(xhr) {
                if (localStorage.token) {
                  xhr.setRequestHeader('Authorization', 'Bearer ' + localStorage.token);
                }
            },
            success: function(res) {
                
                        console.log(res);
                        localStorage.chatid = res.chat_id;
                        //console.log(localStorage.chatid);
                        let dom = document.querySelector(".container_new");
                        dom.remove();
                                

                        let new_dom = document.createElement("div");
                        let a_atr = document.createAttribute("class");
                        a_atr.value = "container";
                        new_dom.setAttributeNode(a_atr);

                        new_dom.innerHTML = newDOM;
                        document.body.appendChild(new_dom);
                        
                        btn = document.getElementById("rec");
                        msg = document.getElementById("msg_inp");
                        exit = document.getElementById("exit");
                        btn.addEventListener("click", function(){
                            let text = msg.value;
                            send(text);
                            msg.value = "";
                        });
                        
                        $('#msg_inp').keypress(function(event){
                            var keycode = (event.keyCode ? event.keyCode : event.which);
                            if(keycode == '13'){
                                let text = msg.value;
                                send(text);
                                msg.value = ""; 
                            }
                        });
                        exit.addEventListener("click",function(){
                            Logout();
                        })

                        window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
                        let finalTranscript = '';
                        let recognition = new window.SpeechRecognition();
                        recognition.interimResults = true;
                        recognition.maxAlternatives = 10;
                        recognition.continuous = false;
                        recognition.onresult = (event) => {
                        let interimTranscript = '';
                        for (let i = event.resultIndex, len = event.results.length; i < len; i++) {
                                let transcript = event.results[i][0].transcript;
                                if (event.results[i].isFinal) {
                                finalTranscript = transcript;
                                } else {
                                interimTranscript = transcript;
                                }
                            }
                            msg.value = "";
                            msg.value = finalTranscript;
                        }
                    
                        mike.addEventListener("click",function(){
                            recognition.start();
                        })

                        // Autocomplete
                        Autocomplete();

            },
            error: function() {
                //alert("Chat instance not created")
            }
        }
    );
}




function print_loading(msg){

    let bot_res = document.getElementById("chatArea");

                            let a = document.createElement("div");
                            let a_atr = document.createAttribute("class");
                            a_atr.value = "chat friend";
                            a.setAttributeNode(a_atr);
                            
                            let b = document.createElement("div");
                            let b_atr = document.createAttribute("class");
                            b_atr.value = "user-photo";
                            b.setAttributeNode(b_atr);
                            
                            let img = document.createElement("img");
                            let i_atr = document.createAttribute("src");
                            i_atr.value = "Images/face.png";
                            img.setAttributeNode(i_atr);
                            
                            b.appendChild(img);
                            
                            let c = document.createElement("div");
                            let c_atr = document.createAttribute("class");
                            c_atr.value = "chat-message";


                            let im = document.createElement("img");
                            let im_atr = document.createAttribute("src");
                            im_atr.value = "Images/loading.gif";
                            im.setAttributeNode(im_atr);
                            
                            im.style.cssText = 'border-radius: 20px; margin: 10px';

                            c.appendChild(im)
                            
                            a.appendChild(b);
                            a.appendChild(c);
                            bot_res.appendChild(a);
}



function print_bot(msg){


    for(let i=0; i<(100000); i++){
        console.log(10);
    }
    let bot_res = document.getElementById("chatArea");

                            let a = document.createElement("div");
                            let a_atr = document.createAttribute("class");
                            a_atr.value = "chat friend";
                            a.setAttributeNode(a_atr);
                            
                            let b = document.createElement("div");
                            let b_atr = document.createAttribute("class");
                            b_atr.value = "user-photo";
                            b.setAttributeNode(b_atr);
                            
                            let img = document.createElement("img");
                            let i_atr = document.createAttribute("src");
                            i_atr.value = "Images/face.png";
                            img.setAttributeNode(i_atr);
                            
                            b.appendChild(img);
                            
                            let c = document.createElement("p");
                            let c_atr = document.createAttribute("class");
                            c_atr.value = "chat-message";
                            c.setAttributeNode(c_atr);
                            c.innerHTML = msg; 
                            
                            a.appendChild(b);
                            a.appendChild(c);


                            bot_res.lastChild.remove();

                            bot_res.appendChild(a);

}


function print_self(msg){


    let bot_res = document.getElementById("chatArea");

                            let a = document.createElement("div");
                            let a_atr = document.createAttribute("class");
                            a_atr.value = "chat self";
                            a.setAttributeNode(a_atr);
                            
                            
                            let c = document.createElement("p");
                            let c_atr = document.createAttribute("class");
                            c_atr.value = "chat-message";
                            c.setAttributeNode(c_atr);
                            c.innerHTML = msg; 
                            
                            // a.appendChild(b);
                            a.appendChild(c);
                            bot_res.appendChild(a);

                            print_loading("Waiting")
                    
}




// // Function to send message
// function send(msg){

//     $.ajax(
//         {
//             url: "http://" + ip + "/send",
//             type: "POST",
//             data: JSON.stringify({'message': msg}),
//             contentType: 'application/json;charset=UTF-8',
//             beforeSend: function(xhr) {
//                 if (localStorage.token) {
//                   xhr.setRequestHeader('Authorization', 'Bearer ' + localStorage.token);
//                 }
//             },
//             success: function(res) {
//                 print_self(msg);
//                 let route = "http://" + ip + "/get_message/" + localStorage.chatid;

//                 $.ajax(
//                     {
//                         url: route,
//                         type: "GET",
//                         contentType: 'application/json;charset=UTF-8',
//                         beforeSend: function(xhr) {
//                             if (localStorage.token) {
//                               xhr.setRequestHeader('Authorization', 'Bearer ' + localStorage.token);
//                             }
                            
//                         },
//                         success: function(res) {
//                             console.log(res); 
//                             console.log('Hey thisis it');
//                             console.log(res[0].message);
//                             let bot_response = res[0].message;
                            
//                             print_bot(bot_response);
                            
//                         },
//                         error: function() {
//                             alert("Message Not Sent: Failed Attemp");
//                         }
//                     }
//                 )
//             },
//             error: function() {
//                 alert("Message cannot be sent due to some error");
//             }
//         }
//     );


// }


function send(msg){
    let route = "http://" + ip + "/get_response";
    print_self(msg);
    (chatArea).scrollTop = (chatArea).scrollHeight
    $.ajax(
        {
            url: route,
            type: "POST",
            data: JSON.stringify({'message': msg, 'user': localStorage.userid, 'chat': localStorage.chatid}),
            contentType: 'application/json;charset=UTF-8',
            beforeSend: function(xhr) {
                if (localStorage.token) {
                  xhr.setRequestHeader('Authorization', 'Bearer ' + localStorage.token);
                }
                
            },
            success: function(res) {
                console.log(res); 
                console.log('Hey thisis it');
                console.log(res.message);
                let bot_response = res.message;
                
                print_bot(bot_response);
                
                
            },
            error: function() {
                alert("Message Not Sent: Failed Attemp");
            }
        }
    )    

}


$(function () {

    
    let name = document.getElementById("name");
    let pass = document.getElementById("pass");
    let login = document.getElementById("login");
    let signup = document.getElementById("signup");
    let btn;
    let msg;
    


    signup.addEventListener("click",function(){

        let n = name.value;
        let p = pass.value;

        Register(n,p);
        console.log(n + " " + p)
    })



    login.addEventListener("click",function(){

        let n = name.value;
        let p = pass.value;
        localStorage.clear();
        Login(n,p);
        
        console.log(n + " " + p) 
    })

    

    chat(localStorage.userid)

})














// Function for Logging in
// function Login (name, pass) {
//     var arr = {'username':name, 'password': pass};
//     $.ajax(
//         {
//                 url: "http://localhost:5000/signin",
//                 type: "POST",
//                 data: JSON.stringify(arr),
//                 contentType: 'application/json;charset=UTF-8',
//                 success: function(res) {
//                     console.log(res);
//                     localStorage.token = res.data.token;
//                     //console.log('Got a token from the server! Token: ' + localStorage.token);
//                     localStorage.userid = res.data.id;
//                     localStorage.name = res.data.username; 
//                     //console.log(localStorage.userid + " " + localStorage.name);
//                 },
//                 error: function() {
//                     alert("Login Failed");
//                 }
//             }
//     );
// }




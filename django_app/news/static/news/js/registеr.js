window.addEventListener('DOMContentLoaded', function(){

     `use strict`;

    let auth = document.querySelectorAll('.register');
    let overlay = document.querySelectorAll('.overlay');
    let close = document.querySelectorAll('.modal_close');
    let log_in = document.querySelector('.log_in');
    let log_register = document.querySelector('.log_register');
    let flash = document.querySelectorAll('.flashed-msg');

    function clears(flash){   
        for(let i = 0; i < flash.length; i++){  
            flash[i].replaceChildren();
        }; 
    };

    function surfacing(i){
        overlay[i].style.display = 'block';
        overlay[i].classList.add("auth-splash");
        document.body.style.overflow = 'hidden';
    };

    function closing(i){
        overlay[i].style.display = 'none';
        overlay[i].classList.remove('auth-splash');
        document.body.style.overflow = ''; 
        clears(flash);       
    };

    auth.forEach((item, i) => {
        item.addEventListener('click', function(event){
            event.preventDefault()
            surfacing(i);
        });
        close[i].addEventListener('click', function(){
            closing(i);
        });
    });

    log_in.addEventListener('click', function(event){
        event.preventDefault()
            closing(0);
            surfacing(1);
        });

    log_register.addEventListener('click', function(event){
        event.preventDefault()  
        closing(1);
        surfacing(0);
    });  
      
    function createFlachMsg(response, i){
        let flash_messeg = document.createElement('div');    
        flash_messeg.classList.add(response.categor);
        flash_messeg.innerHTML= response.messeg;
        flash[i].appendChild(flash_messeg);
    };

    function changes(response){
         if(response.categor == "success"){
            closing(0);
            surfacing(1);
            createFlachMsg(response, 1);
        }else
            {createFlachMsg(response, 0)};
    };

    
    
    let formReg = document.querySelector(".form_reg");
        input = formReg.getElementsByTagName('input');
        formReg.addEventListener('submit', function(event){
            event.preventDefault();
            clears(flash);
            let response =  fetch('/register', {
                    method: 'POST',
                    body: new FormData(formReg),               
                })         
                .then(response => response.json())
                .then(flash_msg => changes(flash_msg))
                .catch(err => console.log(err))  
        });



    /**    
    let formAuth = document.querySelector('.form_auth');
        input = formAuth.getElementsByTagName('input');
        formAuth.addEventListener('submit', function(event){
            event.preventDefault();
            clears(flash);
            let response =  fetch('/login', {
                    method: 'POST',
                    body: new FormData(formAuth),               
                }).then(response => authorization(response)) 

                 .catch(response => auth_msg(response.json()))
                         
                    
           

           
        });

        function auth_msg(data){
            
            console.log(data)
            createFlachMsg(json, 1);
        };

        function authorization(response){
            if (response.redirected){
                window.location.href = response.url;
            }
        }

**/

});



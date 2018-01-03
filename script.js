var arr=['Sushi Tastes Good','Sushi Is Amazing','Sushi is Delicious','Sushi Is Sugoi'];
var i =0;
var heading = document.querySelector('#heading');

    function slide(){
        heading.innerHTML = arr[i];
        //opactiy 1
        heading.style.opacity = 1;
        
        
        // 2 secs call fn
        setTimeout(next, 2000);
    }
    
    console.log(arr.length);
    
    function next (){
        console.log('after 2 seconds')
        //inc for next time in array
        i++;
        
        if(i > arr.length-1){
            i=0
            
        }
        
        //opacity 0
        heading.style.opacity = 0;
        
        //loop
        setTimeout(slide, 1000);
    }
    
    slide();
    
    
        
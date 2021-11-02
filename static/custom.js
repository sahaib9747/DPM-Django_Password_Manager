//display  model on click
 
const modelWrapper = document.querySelector(".models-wrapper");
if (modelWrapper){
    function displaymodel(id){
        const model = document.getElementById(id);
        modelWrapper.style.display = "flex";
        model.style.display = "flex";
        //close model
        const close = document.getElementById("close-model");
        close.addEventListener("click", () =>{
            modelWrapper.style.display = "none";
            model.style.display = "none";
        //I added this later
        document.querySelector("header").style.display = "unset";
        })

        //I added this later
        document.querySelector("header").style.display = "none";
    }
}


//copy to clipboard
const copies = document.querySelectorAll(".copy");
copies.forEach(copy =>{
    copy.onclick = () =>{
        let elemntToCopy = copy.previousElementSibling;
        elemntToCopy.select();
        document.execCommand("copy");
    }
})


//Display the actions of the password card for mobile devices
const actions = document.querySelectorAll(".actions");
if (actions){
    actions.forEach(action =>{
        action.onclick = () =>{
            const links = action.querySelectorAll("a");
            links.forEach(link =>{
                link.style.display = "flex";
            })
            setTimeout(function(){
                links.forEach(link =>{
                    link.style.display = "none";
                })}
            , 3000)
        }
    })
}
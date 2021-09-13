setTimeout(() => {console.log("this is the first message")}, 1500)
setTimeout(() => {console.log("this is the second message")}, 1200);
setTimeout(() => {console.log("this is the third message")}, 1000);


const newPromise = new Promise((resolve, reject) => {
    
    resolve(setTimeout(()=>{ console.log("this is the first message")}, 1500));
});

newPromise.then(()=>{
    setTimeout(() => {console.log("this is the second message")}, 1200);
}).then((resolve) => {
    setTimeout(() => {console.log("this is the third message")}, 1000);
});


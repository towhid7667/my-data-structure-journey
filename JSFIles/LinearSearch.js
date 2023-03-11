const linearSearch = (arr, target) =>{
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === target){
            return `The number is in the position of ${i}`
        }
    }
    return "Not Found"
}


const arr = [4, 2, 5, 9, 1, 3];
const target = 1;
console.log(linearSearch(arr, target))
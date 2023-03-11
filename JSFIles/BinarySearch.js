const binarySearch = (arr , target) => {
    let left = 0;
    let right = arr.length;

    while(left <= right){
        let mid = Math.floor((left + right) / 2)
        
        if(arr[mid] === target){
            return `found at ${mid}`
        }
        else if(arr[mid] < target){
            left = mid + 1
        }
        else{
            right = mid - 1
        }
    }

    return "Not found"
}

const arr = [1, 2,3,4, 5, 6, 7,8];
const target = 7;
console.log(binarySearch(arr, target))
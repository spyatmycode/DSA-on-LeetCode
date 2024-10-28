/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let output = ""
    let string = `${x}`
    let sign = null

    if(string[0] === "-"){
        sign = "-"
    }


    for(let i = string.length - 1; i>=0; i --){
        
        output+= string[i]
    }

   

    let final = parseInt(output)
    if(sign !== null){
        final = -final
    }
    if((final > (Math.pow(2,31) - 1 )) || (final < Math.pow(-2,31))){
        final = 0
    }
    

    return final
};
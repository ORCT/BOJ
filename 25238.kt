import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    var a = sc.nextInt()
    var b = sc.nextInt()
    var result = a * (100 - b) / 100
    if (result >= 100){
        println("0")
    }
    else {
        println("1")
    }
}

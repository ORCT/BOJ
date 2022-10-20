import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)){
    var n = nextBigInteger()
    var m = nextBigInteger()
    var k = nextBigInteger()
    println("${k/m} ${k%m}")
}
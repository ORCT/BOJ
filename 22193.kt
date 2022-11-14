import java.math.BigInteger

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.`out`.bufferedWriter()
    var n = br.readLine()
    var a:BigInteger = BigInteger(br.readLine())
    var b:BigInteger = BigInteger(br.readLine())

    println(a*b)
}
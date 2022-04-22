import scala.language.implicitConversions
import Complex._

object DemoComplex {

  implicit def changeDoubleToComplex(x: Double): Complex = {
    new Complex(x, 0.0)
  }

  def main(args:Array[String]):Unit = {

    val zA = new Complex(-6.0, 1.0)
    //zA: Complex = -6.0 + 1.0 i
    println(zA)

    val zB = Complex(5.0, 1.0)
    //zB: Complex = 5.0 + 1.0 i
    println(zB)

    val zC = Complex(3.0)
    //zC: Complex = 3.0
    println(zC)

    val a = zA * conj(zA)
    //a: Complex = 37.0
    println(a)

    val b = abs(5.0 * zA + 7.0 * zB)
    //b: Double = 13.0
    println(b)

    println(b.isInstanceOf[Double])
    
  }

}

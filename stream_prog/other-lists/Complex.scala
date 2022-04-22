
import scala.math._

class Complex(xx: Double = 0.0, yy: Double = 0.0) {

  var x = xx
  var y = yy

  def this(x: Double) = this(x, 0.0)

  override def toString: String = if(y==0.0) s"$x" else s"$x + $y"+"i"

  def + (com: Complex): Complex = new Complex(this.x + com.x, this.y + com.y)

  def - (com: Complex): Complex = new Complex(this.x - com.x, this.y - com.y)

  def * (com: Complex): Complex = new Complex(this.x * com.x - this.y * com.y, this.x * com.y + this.y * com.x)

  def / (com: Complex): Complex = new Complex((this.x * com.x + this.y * com.y) / (com.x * com.x + com.y * com.y), (this.y * com.x - this.x * com.y) / (com.x * com.x + com.y * com.y))

  def abs (): Double = sqrt(this.x * this.x + this.y * this.y)

  def conj (): Complex = new Complex(this.x, (-1) * this.y)

}

object Complex {
  def apply(x: Double = 0.0, y: Double = 0.0): Complex = {
    var com = new Complex
    com.x = x
    com.y = y
    com
  }
  def conj(com: Complex) = com.conj()
  def abs(com: Complex) = com.abs()


}

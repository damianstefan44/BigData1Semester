object Element {

  private class ArrayElement(
    val contents: Array[String]
  ) extends Element

  private class LineElement(s: String) extends Element {
    val contents = Array(s)
    override def width = s.length
    override def height = 1
  }

  private class UniformElement(
    ch: Char,
    override val width: Int,
    override val height: Int
  ) extends Element {
    private val line = ch.toString * width
    def contents = Array.fill(height)(line)
  }

  private class NaturalElement(
    val nom: Int,
    val denom: Int = 1
  ) extends Element {
    private val line = '-'.toString * (if(nom>denom) nom.toString.length else denom.toString.length)

    def contents = if(denom == 1) Array(nom.toString) else Array(nom.toString,line,denom.toString)

    
  }

  def elem(r1: Rational): Element = new NaturalElement(r1.numer,r1.denom)

  def elem(contents:  Array[String]): Element =
    new ArrayElement(contents)

  def elem(chr: Char, width: Int, height: Int): Element =
    new UniformElement(chr, width, height)

  def elem(line: String): Element = new LineElement(line)

  def elem(nom: Int,denom: Int): Element =
    new NaturalElement(nom, denom)


}

import Element.elem

abstract class Element {
  def contents:  Array[String]
  def width: Int = contents(0).length
  def height: Int = contents.length

  def above(that: Element): Element = {
    val this1 = this widen that.width
    val that1 = that widen this.width
    elem(this1.contents ++ that1.contents)
  }

  def beside(that: Element): Element = {
    val this1 = this heighten that.height
    val that1 = that heighten this.height
    elem(
      for ((line1, line2) <- this1.contents zip that1.contents)
      yield line1 + line2)
  }

  def widen(w: Int): Element =
    if (w <= width) this
    else {
      val left = elem(' ', (w - width) / 2, height)
      val right = elem(' ', w - width - left.width, height)
      left beside this beside right
    }

  def heighten(h: Int): Element =
    if (h <= height) this
    else {
      val top = elem(' ', width, (h - height) / 2)
      val bot = elem(' ', width, h - height - top.height)
      top above this above bot
    }

  def + (that: Element): Element = {

    this beside elem("+") beside that

  }

  def equals (that: Element): Element = {

    this beside elem("=") beside that

  }

  override def toString = contents mkString "\n"
}

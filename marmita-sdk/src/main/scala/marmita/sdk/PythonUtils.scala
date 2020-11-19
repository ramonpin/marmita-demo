package marmita.sdk

import java.util.{List => JList}
import scala.jdk.CollectionConverters._

object PythonUtils {

  def toSeq[T](vs: JList[T]): Seq[T] = vs.asScala.toSeq
  def toList[T](vs: JList[T]): List[T] = vs.asScala.toList
  def toArray[T](vs: JList[T]): Array[T] = vs.toArray().asInstanceOf[Array[T]]
  def toScalaMap[K, V](jm: java.util.Map[K, V]): Map[K, V] = jm.asScala.toMap

  def toJavaList[T](vs: Seq[T]): JList[T] = vs.asJava

}

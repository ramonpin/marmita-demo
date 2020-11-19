package marmita.sdk.tests

import marmita.sdk.App.check

import org.junit.Assert.assertThat
import org.junit.Test
import org.hamcrest.CoreMatchers._

class AppTests {

    @Test
    def testMain(): Unit = {
        assertThat(false, is(false))
    }

    @Test
    def testReversed(): Unit = {
        assertThat(check(true), is(false))
    }

    @Test
    def testSum(): Unit = {
        assertThat(List(1, 2, 3).sum, is(6))
    }
}

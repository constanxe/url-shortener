import { shallowMount } from '@vue/test-utils'
import ShortenedUrlResult from '@/components/ShortenedUrlResult.vue'

describe('ShortenedUrlResult.vue', () => {
  it('renders props.shortenedUrl when passed', () => {
    const shortenedUrl = 'url'
    const wrapper = shallowMount(ShortenedUrlResult, {
      propsData: { shortenedUrl }
    })
    expect(wrapper.text()).toMatch(shortenedUrl)
  })
})

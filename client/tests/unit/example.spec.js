import { mount, shallowMount } from '@vue/test-utils'
import ShortenedUrlResult from '@/components/ShortenedUrlResult.vue'

describe('ShortenedUrlResult.vue', () => {
  let wrapper
  let shortenedUrl = 'url'

  beforeEach(() => wrapper = shallowMount(
    ShortenedUrlResult, {
      propsData: {shortenedUrl}
    }
  ))

  it('renders props.shortenedUrl when passed', () => {
    expect(wrapper.find(`a[href="${shortenedUrl}"]`).exists()).toBeTruthy()
    expect(wrapper.text()).toMatch('Shortened URL: ' + shortenedUrl)
  })

  it('does not show content when props.shortenedUrl is empty', () => {
    const wrapper = shallowMount(ShortenedUrlResult, {
      propsData: {shortenedUrl: ''}
    })
    expect(wrapper.text()).toEqual('')
  })

})

import { mount, shallowMount } from '@vue/test-utils'
import ShortenedUrlResult from '@/components/ShortenedUrlResult.vue'

Object.assign(navigator, {
  clipboard: {
    writeText: jest.fn(),
  },
})

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

  it('copies props.shortenedUrl when button is clicked', () => {
    wrapper.find('button').trigger('click')
    expect(navigator.clipboard.writeText).toHaveBeenCalledWith(shortenedUrl)
  })
})

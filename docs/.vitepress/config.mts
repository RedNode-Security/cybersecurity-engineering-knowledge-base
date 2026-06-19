import { defineConfig } from 'vitepress'

const repo = 'https://github.com/RedNode-Security/cybersecurity-engineering-handbook'

export default defineConfig({
  title: 'Cybersecurity Engineering Handbook',
  description: 'A practical cybersecurity engineering reference for detection, response, threat intelligence, automation, and architecture.',
  lang: 'en-US',
  base: '/cybersecurity-engineering-handbook/',
  cleanUrls: true,
  lastUpdated: true,

  head: [
    ['meta', { name: 'theme-color', content: '#b91c1c' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'Cybersecurity Engineering Handbook' }],
    ['meta', { property: 'og:description', content: 'A practical cybersecurity engineering reference for defenders, analysts, engineers, and researchers.' }]
  ],

  markdown: {
    lineNumbers: true
  },

  themeConfig: {
    siteTitle: 'Cybersecurity Engineering Handbook',
    nav: [
      { text: 'Start Here', link: '/start-here' },
      { text: 'Published', link: '/published-references' },
      { text: 'Detection Library', link: '/detection-library' },
      { text: 'Roadmap', link: '/site-roadmap' },
      { text: 'GitHub', link: repo }
    ],
    sidebar: [
      {
        text: 'Handbook',
        items: [
          { text: 'Home', link: '/' },
          { text: 'Start Here', link: '/start-here' },
          { text: 'Published References', link: '/published-references' },
          { text: 'Detection Library', link: '/detection-library' },
          { text: 'Site Roadmap', link: '/site-roadmap' }
        ]
      }
    ],
    search: { provider: 'local' },
    outline: { level: [2, 3], label: 'On this page' },
    socialLinks: [{ icon: 'github', link: repo }],
    footer: {
      message: 'Documentation: CC BY-SA 4.0. Code: MIT.',
      copyright: 'Copyright © 2026 RedNode Security'
    }
  }
})

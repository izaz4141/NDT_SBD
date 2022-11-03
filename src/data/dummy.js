import avatar_g1 from '../assets/avatar_g1.jpg'
import avatar_g2 from '../assets/avatar_g2.jpg'

export const links = [
  {
    title: 'Dashboard',
    children: [
      {
        name: 'home',
        url: '/',
        icon: 'game-icons:campfire',
        component: import('../views/HomePage.vue'),
      },
      {
        name: 'about',
        url: '/about',
        icon: 'bi:question-circle',
        component: import('../views/AboutPage.vue'),
      },
    ],
  },
  {
    title: 'DevTools',
    children: [
      {
        name: 'developer',
        url: '/dev',
        icon: 'mdi:toolbox',
        component: import('../views/DevPage.vue'),
      },
      {
        name: 'user-list',
        url: '/dev/user_list',
        icon: 'fa-solid:users-cog',
        component: import('../views/UserList.vue'),
      },
    ],
  },
]

export const chatData = [
  {
    image: avatar_g1,
    message: 'Roman Joined the Team!',
    desc: 'Congratulate him',
    time: '9:08 AM',
  },
  {
    image: avatar_g2,
    message: 'New message received',
    desc: 'Salma sent you new message',
    time: '11:56 AM',
  },
]
export const userProfileData = [
  {
    icon: 'carbon:currency',
    title: 'My Profile',
    desc: 'Account Settings',
    iconColor: '#03C9D7',
    iconBg: '#E5FAFB',
  },
  {
    icon: 'tabler:shield-half-filled',
    title: 'My Inbox',
    desc: 'Messages & Emails',
    iconColor: 'rgb(0, 194, 146)',
    iconBg: 'rgb(235, 250, 242)',
  },
  {
    icon: 'jam:credit-card-f',
    title: 'My Tasks',
    desc: 'To-do and Daily Tasks',
    iconColor: 'rgb(255, 244, 229)',
    iconBg: 'rgb(254, 201, 15)',
  },
]

export const themeColors = [
  {
    name: 'blue-theme',
    color: '#1A97F5',
  },
  {
    name: 'green-theme',
    color: '#03C9D7',
  },
  {
    name: 'purple-theme',
    color: '#7352FF',
  },
  {
    name: 'red-theme',
    color: '#FF5C8E',
  },
  {
    name: 'indigo-theme',
    color: '#1E4DB7',
  },
  {
    color: '#FB9678',
    name: 'orange-theme',
  },
]

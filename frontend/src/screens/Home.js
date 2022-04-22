import React, { useEffect } from 'react'

export default function Home() {
  useEffect(() => {
    console.log('Component mounted')
  })

  return <div>Home</div>
}

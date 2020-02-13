---
layout: post
title: "evpn topic list"
published: true
created:  2020 Feb 13 04:42:11 PM
tags: [evpn, bgp, vxlan]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# bgp vxlan evpn topic list

    |EVPN basics
    . |spine and leaves topology
    . |vxlan (overlay) basics
    . . |vlan limitation
    . . |vxlan format
    . . |how it works: vtep
    . . |how VTEP discovery works
    . |route/mac learning mode
    . |DCI options
    . |give some mp-bgp vxlan lab studies
    |evpn concepts
    |evpn benefit
    |evpn terms
    |evpn sevice mode
    . |vlan-based
    . |vlan bundle
    . |vlan-aware bundle
    |evpn route format
    |evpn type 1 route: AD/ESI|EVI
    . |AD per ESI
    . |AD per-EVI (optional)
    . |fast convergence
    . |loop prevention (via type1+type4?)
    . |aliasing (via type1+type2)
    |evpn type 2 route: MAC/VNI
    . |Host MAC/IP Synchronization
    . |Default Gateway Synchronization
    . |MAC Mobility
    |evpn type 3 route: IM/VNI
    |evpn type 4 route: segment/VNI
    |evpn type 5 route: IP prefix, replace L3vpn
    |evpn type 6 selective muticast ethernet route tag
    |evpn type 7 IGMP join synch
    |evpn type 8 IGMP-leave sync
    |other evpn features?
       |evpn extended communities
       |evpn junos config block

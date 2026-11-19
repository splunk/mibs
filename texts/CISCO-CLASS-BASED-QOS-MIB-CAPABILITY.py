#
# PySNMP MIB module CISCO-CLASS-BASED-QOS-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CLASS-BASED-QOS-MIB-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCBQosMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 525))
ciscoCBQosMibCapability.setRevisions(('2007-07-17 00:00', '2006-11-08 00:00', '2005-06-22 00:00', '2004-09-01 00:00', '2003-01-24 00:00', '2001-06-13 00:00', '2000-12-01 00:00', '2000-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCBQosMibCapability.setRevisionsDescriptions(('Added capability statements: \n         ciscoCBQosMibCapV12R0218SXFPCat6KPfc2,\n         ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 and\n         ciscoCBQosMibCapV12R0233SXHPCat6K.', 'Added agent capabilities for\n        Cisco IOS XR 3.4 on CRS-1\n        platform', 'Added agent capabilities for\n        Cisco IOS XR 3.2.0 on CRS-1\n        platform', 'Added agent capabilities for 12.0(29)S.\n        Added agent capabilities for \n        12.2(RLS7)S.', 'Added agent capabilities for\n        Catalyst 8540MSR platform.', 'Added agent capabilities for Mainline.\n        Modified capabilities for T train.', 'Added agent capabilities for T train.', 'The capabilities description of\n        Cisco Class Based QoS MIB.',))
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setLastUpdated('200707170000Z')
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-qos@cisco.com')
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setDescription('Agent capabilities for CISCO-CLASS-BASED-QOS-MIB.')
ciscoCBQosMibCapabilityV121R02E7500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R02E7500 = ciscoCBQosMibCapabilityV121R02E7500.setProductRelease('Cisco IOS 12.1(2)E on 7500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R02E7500 = ciscoCBQosMibCapabilityV121R02E7500.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV121R02E7500.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV120R12S7500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV120R12S7500 = ciscoCBQosMibCapabilityV120R12S7500.setProductRelease('Cisco IOS 12.0(12)S on 7500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV120R12S7500 = ciscoCBQosMibCapabilityV120R12S7500.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV120R12S7500.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV121R05T7200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R05T7200 = ciscoCBQosMibCapabilityV121R05T7200.setProductRelease('Cisco IOS 12.1(5)T for 7200/lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R05T7200 = ciscoCBQosMibCapabilityV121R05T7200.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV121R05T7200.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV122R01T7200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV122R01T7200 = ciscoCBQosMibCapabilityV122R01T7200.setProductRelease('Cisco IOS 12.2(2)T on 7200 and lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV122R01T7200 = ciscoCBQosMibCapabilityV122R01T7200.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV122R01T7200.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV123R01T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV123R01T = ciscoCBQosMibCapabilityV123R01T.setProductRelease('Cisco IOS 12.3(1)T on 7500, 7200 and \n                 lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV123R01T = ciscoCBQosMibCapabilityV123R01T.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV123R01T.setDescription('Class-Based QoS MIB  capabilities.')
ciscoCBQosMibCapabilityV121R14EB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R14EB = ciscoCBQosMibCapabilityV121R14EB.setProductRelease('Cisco IOS 12.1(14)EB on Catalyst 8540MSR platform.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R14EB = ciscoCBQosMibCapabilityV121R14EB.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV121R14EB.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV12R0306T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R0306T = ciscoCBQosMibCapabilityV12R0306T.setProductRelease('Cisco IOS 12.3(6)T on 7200 and \n                 lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R0306T = ciscoCBQosMibCapabilityV12R0306T.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV12R0306T.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R02S = ciscoCBQosMibCapabilityV12R02S.setProductRelease('Cisco IOS 12.2S for 7500/7200/lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R02S = ciscoCBQosMibCapabilityV12R02S.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV12R02S.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R00S = ciscoCBQosMibCapabilityV12R00S.setProductRelease('Cisco IOS 12.0S for 7500/7200/lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R00S = ciscoCBQosMibCapabilityV12R00S.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV12R00S.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV320CRS1 = ciscoCBQosMibCapabilityV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV320CRS1 = ciscoCBQosMibCapabilityV320CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV320CRS1.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV3R4CRS1 = ciscoCBQosMibCapabilityV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV3R4CRS1 = ciscoCBQosMibCapabilityV3R4CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV3R4CRS1.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                     and Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                     and Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0233SXHPCat6K = ciscoCBQosMibCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0233SXHPCat6K = ciscoCBQosMibCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapV12R0233SXHPCat6K.setDescription('Class-Based QoS MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CLASS-BASED-QOS-MIB-CAPABILITY", ciscoCBQosMibCapabilityV121R14EB=ciscoCBQosMibCapabilityV121R14EB, ciscoCBQosMibCapabilityV121R02E7500=ciscoCBQosMibCapabilityV121R02E7500, ciscoCBQosMibCapabilityV320CRS1=ciscoCBQosMibCapabilityV320CRS1, ciscoCBQosMibCapabilityV3R4CRS1=ciscoCBQosMibCapabilityV3R4CRS1, ciscoCBQosMibCapV12R0218SXFPCat6KPfc2=ciscoCBQosMibCapV12R0218SXFPCat6KPfc2, ciscoCBQosMibCapV12R0218SXFPCat6KPfc3=ciscoCBQosMibCapV12R0218SXFPCat6KPfc3, ciscoCBQosMibCapability=ciscoCBQosMibCapability, ciscoCBQosMibCapV12R0233SXHPCat6K=ciscoCBQosMibCapV12R0233SXHPCat6K, ciscoCBQosMibCapabilityV122R01T7200=ciscoCBQosMibCapabilityV122R01T7200, ciscoCBQosMibCapabilityV123R01T=ciscoCBQosMibCapabilityV123R01T, ciscoCBQosMibCapabilityV121R05T7200=ciscoCBQosMibCapabilityV121R05T7200, ciscoCBQosMibCapabilityV12R00S=ciscoCBQosMibCapabilityV12R00S, ciscoCBQosMibCapabilityV12R0306T=ciscoCBQosMibCapabilityV12R0306T, ciscoCBQosMibCapabilityV12R02S=ciscoCBQosMibCapabilityV12R02S, PYSNMP_MODULE_ID=ciscoCBQosMibCapability, ciscoCBQosMibCapabilityV120R12S7500=ciscoCBQosMibCapabilityV120R12S7500)

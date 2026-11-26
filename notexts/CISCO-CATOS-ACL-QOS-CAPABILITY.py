#
# PySNMP MIB module CISCO-CATOS-ACL-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CATOS-ACL-QOS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCatOSAclQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 325))
ciscoCatOSAclQosCapability.setRevisions(('2008-03-17 00:00', '2006-06-29 00:00', '2005-09-06 00:00', '2004-06-24 00:00', '2004-01-27 00:00', '2003-12-19 00:00', '2003-08-25 10:00',))
if mibBuilder.loadTexts: ciscoCatOSAclQosCapability.setLastUpdated('200803170000Z')
if mibBuilder.loadTexts: ciscoCatOSAclQosCapability.setOrganization('Cisco Systems, Inc.')
caqCapabilityV08R0101Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc = caqCapabilityV08R0101Cat6KPfc.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc = caqCapabilityV08R0101Cat6KPfc.setStatus('current')
caqCapabilityV08R0101Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc2 = caqCapabilityV08R0101Cat6KPfc2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc2 = caqCapabilityV08R0101Cat6KPfc2.setStatus('current')
caqCapabilityV08R0101Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc3 = caqCapabilityV08R0101Cat6KPfc3.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc3 = caqCapabilityV08R0101Cat6KPfc3.setStatus('current')
caqCapabilityV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat4K = caqCapabilityV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat4K = caqCapabilityV08R0101Cat4K.setStatus('current')
caqCapabilityV08R0301Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc = caqCapabilityV08R0301Cat6KPfc.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc = caqCapabilityV08R0301Cat6KPfc.setStatus('current')
caqCapabilityV08R0301Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc2 = caqCapabilityV08R0301Cat6KPfc2.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc2 = caqCapabilityV08R0301Cat6KPfc2.setStatus('current')
caqCapabilityV08R0301Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc3 = caqCapabilityV08R0301Cat6KPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc3 = caqCapabilityV08R0301Cat6KPfc3.setStatus('current')
caqCapabilityV08R0401Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc = caqCapabilityV08R0401Cat6KPfc.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc = caqCapabilityV08R0401Cat6KPfc.setStatus('current')
caqCapabilityV08R0401Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc2 = caqCapabilityV08R0401Cat6KPfc2.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc2 = caqCapabilityV08R0401Cat6KPfc2.setStatus('current')
caqCapabilityV08R0401Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3 = caqCapabilityV08R0401Cat6KPfc3.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3 = caqCapabilityV08R0401Cat6KPfc3.setStatus('current')
caqCapabilityV08R0401Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3b = caqCapabilityV08R0401Cat6KPfc3b.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3b = caqCapabilityV08R0401Cat6KPfc3b.setStatus('current')
caqCapabilityV08R0501Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc = caqCapabilityV08R0501Cat6KPfc.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc = caqCapabilityV08R0501Cat6KPfc.setStatus('current')
caqCapabilityV08R0501Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc2 = caqCapabilityV08R0501Cat6KPfc2.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc2 = caqCapabilityV08R0501Cat6KPfc2.setStatus('current')
caqCapabilityV08R0501Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3 = caqCapabilityV08R0501Cat6KPfc3.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3 = caqCapabilityV08R0501Cat6KPfc3.setStatus('current')
caqCapabilityV08R0501Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3b = caqCapabilityV08R0501Cat6KPfc3b.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3b = caqCapabilityV08R0501Cat6KPfc3b.setStatus('current')
caqCapabilityV08R0601Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc = caqCapabilityV08R0601Cat6KPfc.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc = caqCapabilityV08R0601Cat6KPfc.setStatus('current')
caqCapabilityV08R0601Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc2 = caqCapabilityV08R0601Cat6KPfc2.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc2 = caqCapabilityV08R0601Cat6KPfc2.setStatus('current')
caqCapabilityV08R0601Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3 = caqCapabilityV08R0601Cat6KPfc3.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3 = caqCapabilityV08R0601Cat6KPfc3.setStatus('current')
caqCapabilityV08R0601Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3b = caqCapabilityV08R0601Cat6KPfc3b.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3b = caqCapabilityV08R0601Cat6KPfc3b.setStatus('current')
caqCapabilityV08R0701Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc = caqCapabilityV08R0701Cat6KPfc.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc = caqCapabilityV08R0701Cat6KPfc.setStatus('current')
caqCapabilityV08R0701Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc2 = caqCapabilityV08R0701Cat6KPfc2.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc2 = caqCapabilityV08R0701Cat6KPfc2.setStatus('current')
caqCapabilityV08R0701Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3 = caqCapabilityV08R0701Cat6KPfc3.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3 = caqCapabilityV08R0701Cat6KPfc3.setStatus('current')
caqCapabilityV08R0701Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3b = caqCapabilityV08R0701Cat6KPfc3b.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3b = caqCapabilityV08R0701Cat6KPfc3b.setStatus('current')
mibBuilder.exportSymbols("CISCO-CATOS-ACL-QOS-CAPABILITY", caqCapabilityV08R0601Cat6KPfc3=caqCapabilityV08R0601Cat6KPfc3, caqCapabilityV08R0101Cat6KPfc3=caqCapabilityV08R0101Cat6KPfc3, caqCapabilityV08R0101Cat6KPfc2=caqCapabilityV08R0101Cat6KPfc2, caqCapabilityV08R0301Cat6KPfc2=caqCapabilityV08R0301Cat6KPfc2, caqCapabilityV08R0401Cat6KPfc2=caqCapabilityV08R0401Cat6KPfc2, caqCapabilityV08R0501Cat6KPfc=caqCapabilityV08R0501Cat6KPfc, caqCapabilityV08R0601Cat6KPfc2=caqCapabilityV08R0601Cat6KPfc2, caqCapabilityV08R0101Cat6KPfc=caqCapabilityV08R0101Cat6KPfc, caqCapabilityV08R0101Cat4K=caqCapabilityV08R0101Cat4K, caqCapabilityV08R0701Cat6KPfc3b=caqCapabilityV08R0701Cat6KPfc3b, caqCapabilityV08R0301Cat6KPfc3=caqCapabilityV08R0301Cat6KPfc3, caqCapabilityV08R0701Cat6KPfc2=caqCapabilityV08R0701Cat6KPfc2, ciscoCatOSAclQosCapability=ciscoCatOSAclQosCapability, PYSNMP_MODULE_ID=ciscoCatOSAclQosCapability, caqCapabilityV08R0401Cat6KPfc3b=caqCapabilityV08R0401Cat6KPfc3b, caqCapabilityV08R0401Cat6KPfc=caqCapabilityV08R0401Cat6KPfc, caqCapabilityV08R0301Cat6KPfc=caqCapabilityV08R0301Cat6KPfc, caqCapabilityV08R0501Cat6KPfc2=caqCapabilityV08R0501Cat6KPfc2, caqCapabilityV08R0601Cat6KPfc3b=caqCapabilityV08R0601Cat6KPfc3b, caqCapabilityV08R0701Cat6KPfc3=caqCapabilityV08R0701Cat6KPfc3, caqCapabilityV08R0501Cat6KPfc3=caqCapabilityV08R0501Cat6KPfc3, caqCapabilityV08R0501Cat6KPfc3b=caqCapabilityV08R0501Cat6KPfc3b, caqCapabilityV08R0701Cat6KPfc=caqCapabilityV08R0701Cat6KPfc, caqCapabilityV08R0601Cat6KPfc=caqCapabilityV08R0601Cat6KPfc, caqCapabilityV08R0401Cat6KPfc3=caqCapabilityV08R0401Cat6KPfc3)

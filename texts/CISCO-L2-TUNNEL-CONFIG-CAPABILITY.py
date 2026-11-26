#
# PySNMP MIB module CISCO-L2-TUNNEL-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L2-TUNNEL-CONFIG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoL2TunnelConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 334))
ciscoL2TunnelConfigCapability.setRevisions(('2010-05-14 00:00', '2008-10-27 00:00', '2007-07-09 00:00', '2005-07-05 00:00', '2004-06-21 00:00', '2003-08-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setRevisionsDescriptions(('Added capability statement\n        cL2TunnelConfigCapV12R0254SGPCat4K.', 'Added capability statement\n        cL2TunnelConfigCapV12R0233SXIPCat6K.', 'Added capability statement\n        cL2TunnelConfigCapV12R0233SXHPCat6k.', 'Added capability statement\n        cL2TunConfCapCatOSV08R0501.', 'Added capability statement\n        cL2TunConfCapCatOSV08R0401Cat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setLastUpdated('201005140000Z')
if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com,\n            cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setDescription('The capabilities description of\n        CISCO-L2-TUNNEL-CONFIG-MIB.')
cL2TunConfCapCatOSV07R0501Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV07R0501Cat6k = cL2TunConfCapCatOSV07R0501Cat6k.setProductRelease('Cisco CatOS 7.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV07R0501Cat6k = cL2TunConfCapCatOSV07R0501Cat6k.setStatus('current')
if mibBuilder.loadTexts: cL2TunConfCapCatOSV07R0501Cat6k.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunnelConfigCapV12R0214SX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0214SX = cL2TunnelConfigCapV12R0214SX.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0214SX = cL2TunnelConfigCapV12R0214SX.setStatus('current')
if mibBuilder.loadTexts: cL2TunnelConfigCapV12R0214SX.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunConfCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV08R0401 = cL2TunConfCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV08R0401 = cL2TunConfCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: cL2TunConfCapCatOSV08R0401.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunConfCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV08R0501 = cL2TunConfCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV08R0501 = cL2TunConfCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: cL2TunConfCapCatOSV08R0501.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunnelConfigCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0233SXHPCat6k = cL2TunnelConfigCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0233SXHPCat6k = cL2TunnelConfigCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cL2TunnelConfigCapV12R0233SXHPCat6k.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunnelConfigCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0233SXIPCat6K = cL2TunnelConfigCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0233SXIPCat6K = cL2TunnelConfigCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cL2TunnelConfigCapV12R0233SXIPCat6K.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunnelConfigCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0254SGPCat4K = cL2TunnelConfigCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches,\n                    except LAN Base images.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0254SGPCat4K = cL2TunnelConfigCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cL2TunnelConfigCapV12R0254SGPCat4K.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-L2-TUNNEL-CONFIG-CAPABILITY", cL2TunConfCapCatOSV08R0401=cL2TunConfCapCatOSV08R0401, cL2TunConfCapCatOSV07R0501Cat6k=cL2TunConfCapCatOSV07R0501Cat6k, PYSNMP_MODULE_ID=ciscoL2TunnelConfigCapability, cL2TunnelConfigCapV12R0214SX=cL2TunnelConfigCapV12R0214SX, cL2TunnelConfigCapV12R0254SGPCat4K=cL2TunnelConfigCapV12R0254SGPCat4K, cL2TunnelConfigCapV12R0233SXIPCat6K=cL2TunnelConfigCapV12R0233SXIPCat6K, cL2TunConfCapCatOSV08R0501=cL2TunConfCapCatOSV08R0501, ciscoL2TunnelConfigCapability=ciscoL2TunnelConfigCapability, cL2TunnelConfigCapV12R0233SXHPCat6k=cL2TunnelConfigCapV12R0233SXHPCat6k)

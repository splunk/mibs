#
# PySNMP MIB module CISCO-IF-EXTENSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IF-EXTENSION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIfExtensionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 395))
ciscoIfExtensionCapability.setRevisions(('2015-06-03 00:00', '2013-09-05 00:00', '2012-03-01 00:00', '2011-03-21 00:00', '2008-03-24 00:00', '2007-11-05 00:00', '2007-08-30 00:00', '2007-04-19 00:00', '2006-02-21 00:00', '2005-04-14 00:00', '2005-03-04 00:00', '2004-01-26 00:00',))
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setOrganization('Cisco Systems, Inc.')
ciscoIfExtensionCapV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionCapV08R0301 = ciscoIfExtensionCapV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionCapV08R0301 = ciscoIfExtensionCapV08R0301.setStatus('current')
ciscoIfExtCapV12R0217bSXAPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0217bSXAPCat6K = ciscoIfExtCapV12R0217bSXAPCat6K.setProductRelease('Cisco IOS 12.2(17b)SXA on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0217bSXAPCat6K = ciscoIfExtCapV12R0217bSXAPCat6K.setStatus('current')
ciscoIfExtCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapSanOSV30R1MDS9000 = ciscoIfExtCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0 on Cisco MDS 9000\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapSanOSV30R1MDS9000 = ciscoIfExtCapSanOSV30R1MDS9000.setStatus('current')
ciscoIfExtCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapabilityACSWV03R000 = ciscoIfExtCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapabilityACSWV03R000 = ciscoIfExtCapabilityACSWV03R000.setStatus('current')
ciscoIfExtCapV12R0229SM1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0229SM1 = ciscoIfExtCapV12R0229SM1.setProductRelease('Cisco IOS 12.2(29)SM1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0229SM1 = ciscoIfExtCapV12R0229SM1.setStatus('current')
ciscoIfExtCapV12R0412MR1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0412MR1 = ciscoIfExtCapV12R0412MR1.setProductRelease('Cisco IOS 12.4(2)MR1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0412MR1 = ciscoIfExtCapV12R0412MR1.setStatus('current')
ciscoIfExtCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0233SXHPCat6K = ciscoIfExtCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0233SXHPCat6K = ciscoIfExtCapV12R0233SXHPCat6K.setStatus('current')
ciscoIfExtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapc4710aceVA1R700 = ciscoIfExtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapc4710aceVA1R700 = ciscoIfExtCapc4710aceVA1R700.setStatus('current')
ciscoIfExtCapCatOSV08R0701PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapCatOSV08R0701PCat6K = ciscoIfExtCapCatOSV08R0701PCat6K.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500 and\n                     Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapCatOSV08R0701PCat6K = ciscoIfExtCapCatOSV08R0701PCat6K.setStatus('current')
ciscoIfExtCapNXOSV52R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNXOSV52R1MDS9000 = ciscoIfExtCapNXOSV52R1MDS9000.setProductRelease('Cisco NXOS 5.2(1) on MDS 9000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNXOSV52R1MDS9000 = ciscoIfExtCapNXOSV52R1MDS9000.setStatus('current')
ciscoIfExtCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV15R0002SGPCat4K = ciscoIfExtCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Catalyst 4000 family\n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV15R0002SGPCat4K = ciscoIfExtCapV15R0002SGPCat4K.setStatus('current')
ciscoIfExtCapNxOSV06R0201PMDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0201PMDS9000 = ciscoIfExtCapNxOSV06R0201PMDS9000.setProductRelease('Cisco NX-OS 6.2(1) on MDS 9000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0201PMDS9000 = ciscoIfExtCapNxOSV06R0201PMDS9000.setStatus('current')
ciscoIfExtCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0202PN7K = ciscoIfExtCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0202PN7K = ciscoIfExtCapNxOSV06R0202PN7K.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-EXTENSION-CAPABILITY", ciscoIfExtCapCatOSV08R0701PCat6K=ciscoIfExtCapCatOSV08R0701PCat6K, ciscoIfExtCapV12R0229SM1=ciscoIfExtCapV12R0229SM1, ciscoIfExtCapSanOSV30R1MDS9000=ciscoIfExtCapSanOSV30R1MDS9000, ciscoIfExtCapNxOSV06R0201PMDS9000=ciscoIfExtCapNxOSV06R0201PMDS9000, PYSNMP_MODULE_ID=ciscoIfExtensionCapability, ciscoIfExtCapabilityACSWV03R000=ciscoIfExtCapabilityACSWV03R000, ciscoIfExtensionCapV08R0301=ciscoIfExtensionCapV08R0301, ciscoIfExtCapc4710aceVA1R700=ciscoIfExtCapc4710aceVA1R700, ciscoIfExtCapV12R0412MR1=ciscoIfExtCapV12R0412MR1, ciscoIfExtCapV12R0217bSXAPCat6K=ciscoIfExtCapV12R0217bSXAPCat6K, ciscoIfExtCapNXOSV52R1MDS9000=ciscoIfExtCapNXOSV52R1MDS9000, ciscoIfExtensionCapability=ciscoIfExtensionCapability, ciscoIfExtCapNxOSV06R0202PN7K=ciscoIfExtCapNxOSV06R0202PN7K, ciscoIfExtCapV15R0002SGPCat4K=ciscoIfExtCapV15R0002SGPCat4K, ciscoIfExtCapV12R0233SXHPCat6K=ciscoIfExtCapV12R0233SXHPCat6K)

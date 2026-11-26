#
# PySNMP MIB module CISCO-CAT6K-CROSSBAR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CAT6K-CROSSBAR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoCat6kCrossbarCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 356))
ciscoCat6kCrossbarCapability.setRevisions(('2013-07-25 00:00', '2010-11-24 00:00', '2010-03-11 00:00', '2008-10-22 00:00', '2008-03-24 00:00', '2008-03-14 00:00', '2007-11-19 00:00', '2007-06-28 00:00', '2007-01-03 00:00', '2005-06-22 00:00', '2005-05-03 00:00', '2004-10-19 00:00', '2004-04-19 00:00', '2004-04-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCat6kCrossbarCapability.setRevisionsDescriptions(('Added capability statement\n        ccXbarCapV15R0102SYPCat6kSup2T and\n        ccXbarCapV15R0102SYPCat6kSup720.', 'Added capability statement\n        ccXbarCapV12R0250SYPCat6K.', 'Added capability statements\n        ccXbarCapV12R0233SXI4PCat6KSup720\n        and ccXbarCapV12R0233SXI4PCat6KSup32.', 'Added capability statements\n        ccXbarCapV12R0233SXIPCat6KSup720\n        and ccXbarCapV12R0233SXIPCat6KSup32.', 'Added capability statement \n        ccXbarCapCatOSV08R0701PCat6KSup2.\n        Modified the description of\n        capability statement\n        ccXbarCapV12R0233SXHPCat6KSup32.', 'Added capability statements \n        ccXbarCapCatOSV08R0701PCat6KSup720\n        and ccXbarCapCatOSV08R0701PCat6KSup32.', 'Added capability statement \n        ccXbarCapV12R0233SXH01PCat6KSup720.', 'Added capability statements\n        ccXbarCapV12R0233SXHPCat6KSup720\n        and ccXbarCapV12R0233SXHPCat6KSup32.', 'Added capability statement\n        ccXbarCapCatOSV08R0601Cat6KSup32.', 'Added capability statements\n        ccXbarCapV12R0218SXFPCat6KSup2,\n        ccXbarCapV12R0218SXFPCat6KSup720,\n        and ccXbarCapV12R0218SXFPCat6KSup32.', 'Added capability statements\n        ccXbarCapV12R012504EPCat6KSup1,\n        and ccXbarCapV12R012504EPCat6KSup2.', 'Added capability statements\n        ccXbarCapV12R0119EPCat6KSup2,\n        ccXbarCapV12R0123E01PCat6KSup1,\n        and ccXbarCapV12R0123E01PCat6KSup2.', 'Added ccXbarCapV12R0218SXDCat6KSup720 and\n        ccXbarCapV12R0218SXDCat6KSup2.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCat6kCrossbarCapability.setLastUpdated('201307250000Z')
if mibBuilder.loadTexts: ciscoCat6kCrossbarCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCat6kCrossbarCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-cat6000@cisco.com')
if mibBuilder.loadTexts: ciscoCat6kCrossbarCapability.setDescription('The capabilities description of\n        CISCO-CAT6K-CROSSBAR-MIB.')
ccXbarCapV12R0108aEXCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0108aEXCat6KSup2 = ccXbarCapV12R0108aEXCat6KSup2.setProductRelease('Cisco IOS 12.1(8a)EX on Catalyst 6000/6500\n                         and Cisco 7600 series devices with \n                         Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0108aEXCat6KSup2 = ccXbarCapV12R0108aEXCat6KSup2.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0108aEXCat6KSup2.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0214SXCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0214SXCat6KSup720 = ccXbarCapV12R0214SXCat6KSup720.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0214SXCat6KSup720 = ccXbarCapV12R0214SXCat6KSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0214SXCat6KSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapCatOSV06R0301Cat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV06R0301Cat6KSup2 = ccXbarCapCatOSV06R0301Cat6KSup2.setProductRelease('Cisco CatOS 6.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices\n                         with Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV06R0301Cat6KSup2 = ccXbarCapCatOSV06R0301Cat6KSup2.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapCatOSV06R0301Cat6KSup2.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapCatOSV08R0101Cat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0101Cat6KSup2 = ccXbarCapCatOSV08R0101Cat6KSup2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices\n                         with Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0101Cat6KSup2 = ccXbarCapCatOSV08R0101Cat6KSup2.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapCatOSV08R0101Cat6KSup2.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapCatOSV08R0101Cat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0101Cat6KSup720 = ccXbarCapCatOSV08R0101Cat6KSup720.setProductRelease('Cisco CatOS 8.1(1) on  Catalyst 6500\n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0101Cat6KSup720 = ccXbarCapCatOSV08R0101Cat6KSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapCatOSV08R0101Cat6KSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0218SXDCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXDCat6KSup720 = ccXbarCapV12R0218SXDCat6KSup720.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXDCat6KSup720 = ccXbarCapV12R0218SXDCat6KSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0218SXDCat6KSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0218SXDCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXDCat6KSup2 = ccXbarCapV12R0218SXDCat6KSup2.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXDCat6KSup2 = ccXbarCapV12R0218SXDCat6KSup2.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0218SXDCat6KSup2.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0119EPCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0119EPCat6KSup2 = ccXbarCapV12R0119EPCat6KSup2.setProductRelease('Cisco IOS 12.1(19)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices with \n                         Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0119EPCat6KSup2 = ccXbarCapV12R0119EPCat6KSup2.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0119EPCat6KSup2.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0123E01PCat6KSup1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0123E01PCat6KSup1 = ccXbarCapV12R0123E01PCat6KSup1.setProductRelease('Cisco IOS 12.1(23)E1 on Catalyst 6000/6500 \n                        series devices with Supervisor 1 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0123E01PCat6KSup1 = ccXbarCapV12R0123E01PCat6KSup1.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0123E01PCat6KSup1.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0123E01PCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0123E01PCat6KSup2 = ccXbarCapV12R0123E01PCat6KSup2.setProductRelease('Cisco IOS 12.1(23)E1 on Catalyst 6000/6500\n                         and Cisco 7600 series devices with \n                         Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0123E01PCat6KSup2 = ccXbarCapV12R0123E01PCat6KSup2.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0123E01PCat6KSup2.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R012504EPCat6KSup1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R012504EPCat6KSup1 = ccXbarCapV12R012504EPCat6KSup1.setProductRelease('Cisco IOS 12.1(25.04)E on Catalyst 6000/6500 \n                        series devices with Supervisor 1 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R012504EPCat6KSup1 = ccXbarCapV12R012504EPCat6KSup1.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R012504EPCat6KSup1.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R012504EPCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R012504EPCat6KSup2 = ccXbarCapV12R012504EPCat6KSup2.setProductRelease('Cisco IOS 12.1(25.04)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices with \n                         Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R012504EPCat6KSup2 = ccXbarCapV12R012504EPCat6KSup2.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R012504EPCat6KSup2.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0218SXFPCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup2 = ccXbarCapV12R0218SXFPCat6KSup2.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup2 = ccXbarCapV12R0218SXFPCat6KSup2.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0218SXFPCat6KSup2.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0218SXFPCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup720 = ccXbarCapV12R0218SXFPCat6KSup720.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup720 = ccXbarCapV12R0218SXFPCat6KSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0218SXFPCat6KSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0218SXFPCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup32 = ccXbarCapV12R0218SXFPCat6KSup32.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup32 = ccXbarCapV12R0218SXFPCat6KSup32.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0218SXFPCat6KSup32.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapCatOSV08R0601Cat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0601Cat6KSup32 = ccXbarCapCatOSV08R0601Cat6KSup32.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6500\n                        series devices with Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0601Cat6KSup32 = ccXbarCapCatOSV08R0601Cat6KSup32.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapCatOSV08R0601Cat6KSup32.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0233SXHPCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXHPCat6KSup720 = ccXbarCapV12R0233SXHPCat6KSup720.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                        series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXHPCat6KSup720 = ccXbarCapV12R0233SXHPCat6KSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0233SXHPCat6KSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0233SXHPCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXHPCat6KSup32 = ccXbarCapV12R0233SXHPCat6KSup32.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                     series devices with Supervisor 32 present\n                     and ME-C65xx series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXHPCat6KSup32 = ccXbarCapV12R0233SXHPCat6KSup32.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0233SXHPCat6KSup32.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0233SXH01PCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXH01PCat6KSup720 = ccXbarCapV12R0233SXH01PCat6KSup720.setProductRelease('Cisco IOS 12.2(33)SXH1 on Catalyst 6000/6500\n                        series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXH01PCat6KSup720 = ccXbarCapV12R0233SXH01PCat6KSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0233SXH01PCat6KSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapCatOSV08R0701PCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup720 = ccXbarCapCatOSV08R0701PCat6KSup720.setProductRelease('Cisco CatOS 8.7(1) on  Catalyst 6000/6500\n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup720 = ccXbarCapCatOSV08R0701PCat6KSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapCatOSV08R0701PCat6KSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapCatOSV08R0701PCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup32 = ccXbarCapCatOSV08R0701PCat6KSup32.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6500\n                     series devices with Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup32 = ccXbarCapCatOSV08R0701PCat6KSup32.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapCatOSV08R0701PCat6KSup32.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapCatOSV08R0701PCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup2 = ccXbarCapCatOSV08R0701PCat6KSup2.setProductRelease('Cisco CatOS 8.7(1) on  Catalyst 6000/6500\n                     and Cisco 7600 series devices with \n                     Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup2 = ccXbarCapCatOSV08R0701PCat6KSup2.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapCatOSV08R0701PCat6KSup2.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0233SXIPCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXIPCat6KSup720 = ccXbarCapV12R0233SXIPCat6KSup720.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXIPCat6KSup720 = ccXbarCapV12R0233SXIPCat6KSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0233SXIPCat6KSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0233SXIPCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXIPCat6KSup32 = ccXbarCapV12R0233SXIPCat6KSup32.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices with Supervisor 32 present\n                     and ME-C65xx series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXIPCat6KSup32 = ccXbarCapV12R0233SXIPCat6KSup32.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0233SXIPCat6KSup32.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0233SXI4PCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXI4PCat6KSup720 = ccXbarCapV12R0233SXI4PCat6KSup720.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXI4PCat6KSup720 = ccXbarCapV12R0233SXI4PCat6KSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0233SXI4PCat6KSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0233SXI4PCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXI4PCat6KSup32 = ccXbarCapV12R0233SXI4PCat6KSup32.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices with Supervisor 32 present\n                     and ME-C65xx series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXI4PCat6KSup32 = ccXbarCapV12R0233SXI4PCat6KSup32.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0233SXI4PCat6KSup32.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0250SYPCat6K = ccXbarCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0250SYPCat6K = ccXbarCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV12R0250SYPCat6K.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV15R0102SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV15R0102SYPCat6kSup2T = ccXbarCapV15R0102SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV15R0102SYPCat6kSup2T = ccXbarCapV15R0102SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV15R0102SYPCat6kSup2T.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
ccXbarCapV15R0102SYPCat6kSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 29))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV15R0102SYPCat6kSup720 = ccXbarCapV15R0102SYPCat6kSup720.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV15R0102SYPCat6kSup720 = ccXbarCapV15R0102SYPCat6kSup720.setStatus('current')
if mibBuilder.loadTexts: ccXbarCapV15R0102SYPCat6kSup720.setDescription('CISCO-CAT6K-CROSSBAR-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CAT6K-CROSSBAR-CAPABILITY", PYSNMP_MODULE_ID=ciscoCat6kCrossbarCapability, ccXbarCapV12R0218SXFPCat6KSup32=ccXbarCapV12R0218SXFPCat6KSup32, ccXbarCapV12R0218SXDCat6KSup720=ccXbarCapV12R0218SXDCat6KSup720, ccXbarCapV12R0233SXHPCat6KSup32=ccXbarCapV12R0233SXHPCat6KSup32, ccXbarCapV12R012504EPCat6KSup2=ccXbarCapV12R012504EPCat6KSup2, ccXbarCapV12R0233SXH01PCat6KSup720=ccXbarCapV12R0233SXH01PCat6KSup720, ccXbarCapV12R0123E01PCat6KSup1=ccXbarCapV12R0123E01PCat6KSup1, ccXbarCapCatOSV08R0701PCat6KSup2=ccXbarCapCatOSV08R0701PCat6KSup2, ccXbarCapV12R0218SXFPCat6KSup720=ccXbarCapV12R0218SXFPCat6KSup720, ccXbarCapV12R0233SXIPCat6KSup32=ccXbarCapV12R0233SXIPCat6KSup32, ccXbarCapV12R0233SXI4PCat6KSup720=ccXbarCapV12R0233SXI4PCat6KSup720, ccXbarCapCatOSV08R0101Cat6KSup720=ccXbarCapCatOSV08R0101Cat6KSup720, ccXbarCapV12R0233SXI4PCat6KSup32=ccXbarCapV12R0233SXI4PCat6KSup32, ccXbarCapV12R0250SYPCat6K=ccXbarCapV12R0250SYPCat6K, ccXbarCapV12R012504EPCat6KSup1=ccXbarCapV12R012504EPCat6KSup1, ccXbarCapV12R0218SXDCat6KSup2=ccXbarCapV12R0218SXDCat6KSup2, ccXbarCapV12R0214SXCat6KSup720=ccXbarCapV12R0214SXCat6KSup720, ccXbarCapCatOSV08R0101Cat6KSup2=ccXbarCapCatOSV08R0101Cat6KSup2, ccXbarCapV12R0108aEXCat6KSup2=ccXbarCapV12R0108aEXCat6KSup2, ccXbarCapV12R0119EPCat6KSup2=ccXbarCapV12R0119EPCat6KSup2, ccXbarCapCatOSV08R0701PCat6KSup32=ccXbarCapCatOSV08R0701PCat6KSup32, ccXbarCapV12R0218SXFPCat6KSup2=ccXbarCapV12R0218SXFPCat6KSup2, ccXbarCapCatOSV06R0301Cat6KSup2=ccXbarCapCatOSV06R0301Cat6KSup2, ccXbarCapV12R0233SXHPCat6KSup720=ccXbarCapV12R0233SXHPCat6KSup720, ccXbarCapV15R0102SYPCat6kSup720=ccXbarCapV15R0102SYPCat6kSup720, ccXbarCapCatOSV08R0601Cat6KSup32=ccXbarCapCatOSV08R0601Cat6KSup32, ccXbarCapV15R0102SYPCat6kSup2T=ccXbarCapV15R0102SYPCat6kSup2T, ciscoCat6kCrossbarCapability=ciscoCat6kCrossbarCapability, ccXbarCapCatOSV08R0701PCat6KSup720=ccXbarCapCatOSV08R0701PCat6KSup720, ccXbarCapV12R0123E01PCat6KSup2=ccXbarCapV12R0123E01PCat6KSup2, ccXbarCapV12R0233SXIPCat6KSup720=ccXbarCapV12R0233SXIPCat6KSup720)

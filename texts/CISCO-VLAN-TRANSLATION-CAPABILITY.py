#
# PySNMP MIB module CISCO-VLAN-TRANSLATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-TRANSLATION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVlanTranslationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 405))
ciscoVlanTranslationCapability.setRevisions(('2012-01-09 00:00', '2006-02-08 00:00', '2004-08-11 00:00', '2004-06-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setRevisionsDescriptions(('Add capability statement\n        cVlanTransCapV15R0001SYPCat6kSup2T', 'Correct cVlanTransCapV12R0218SXD1Cat6K\n        to cVlanTransCapV12R0218SXEPCat6K', 'Add capability statement\n        cVlanTransCapV12R0218SXD1Cat6K', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setLastUpdated('201201090000Z')
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setDescription('The capabilities description of\n        CISCO-VLAN-TRANSLATION-MIB.')
cVlanTranslationCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTranslationCapCatOSV08R0401 = cVlanTranslationCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTranslationCapCatOSV08R0401 = cVlanTranslationCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: cVlanTranslationCapCatOSV08R0401.setDescription('CISCO-VLAN-TRANSLATION-MIB capabilities.')
cVlanTransCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV12R0218SXEPCat6K = cVlanTransCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV12R0218SXEPCat6K = cVlanTransCapV12R0218SXEPCat6K.setStatus('current')
if mibBuilder.loadTexts: cVlanTransCapV12R0218SXEPCat6K.setDescription('CISCO-VLAN-TRANSLATION-MIB capabilities.')
cVlanTransCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV15R0001SYPCat6kSup2T = cVlanTransCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV15R0001SYPCat6kSup2T = cVlanTransCapV15R0001SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: cVlanTransCapV15R0001SYPCat6kSup2T.setDescription('CISCO-VLAN-TRANSLATION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VLAN-TRANSLATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoVlanTranslationCapability, cVlanTransCapV12R0218SXEPCat6K=cVlanTransCapV12R0218SXEPCat6K, cVlanTranslationCapCatOSV08R0401=cVlanTranslationCapCatOSV08R0401, ciscoVlanTranslationCapability=ciscoVlanTranslationCapability, cVlanTransCapV15R0001SYPCat6kSup2T=cVlanTransCapV15R0001SYPCat6kSup2T)

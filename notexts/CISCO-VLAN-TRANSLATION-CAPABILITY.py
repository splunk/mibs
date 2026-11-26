#
# PySNMP MIB module CISCO-VLAN-TRANSLATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-TRANSLATION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
ciscoVlanTranslationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 405))
ciscoVlanTranslationCapability.setRevisions(('2012-01-09 00:00', '2006-02-08 00:00', '2004-08-11 00:00', '2004-06-07 00:00',))
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setLastUpdated('201201090000Z')
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setOrganization('Cisco Systems, Inc.')
cVlanTranslationCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTranslationCapCatOSV08R0401 = cVlanTranslationCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTranslationCapCatOSV08R0401 = cVlanTranslationCapCatOSV08R0401.setStatus('current')
cVlanTransCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV12R0218SXEPCat6K = cVlanTransCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV12R0218SXEPCat6K = cVlanTransCapV12R0218SXEPCat6K.setStatus('current')
cVlanTransCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV15R0001SYPCat6kSup2T = cVlanTransCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV15R0001SYPCat6kSup2T = cVlanTransCapV15R0001SYPCat6kSup2T.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-TRANSLATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoVlanTranslationCapability, cVlanTranslationCapCatOSV08R0401=cVlanTranslationCapCatOSV08R0401, cVlanTransCapV15R0001SYPCat6kSup2T=cVlanTransCapV15R0001SYPCat6kSup2T, ciscoVlanTranslationCapability=ciscoVlanTranslationCapability, cVlanTransCapV12R0218SXEPCat6K=cVlanTransCapV12R0218SXEPCat6K)

#
# PySNMP MIB module CISCO-VLAN-TRANSLATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-TRANSLATION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("CISCO-VLAN-TRANSLATION-CAPABILITY", ciscoVlanTranslationCapability=ciscoVlanTranslationCapability, cVlanTranslationCapCatOSV08R0401=cVlanTranslationCapCatOSV08R0401, PYSNMP_MODULE_ID=ciscoVlanTranslationCapability, cVlanTransCapV12R0218SXEPCat6K=cVlanTransCapV12R0218SXEPCat6K, cVlanTransCapV15R0001SYPCat6kSup2T=cVlanTransCapV15R0001SYPCat6kSup2T)

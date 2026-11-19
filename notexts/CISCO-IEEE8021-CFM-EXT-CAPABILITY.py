#
# PySNMP MIB module CISCO-IEEE8021-CFM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IEEE8021-CFM-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8021CfmExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 576))
ciscoIeee8021CfmExtCapability.setRevisions(('2008-12-05 00:00',))
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setLastUpdated('200812050000Z')
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoIeee8021CfmExtCapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 576, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmExtCapCatOSV08R0702 = ciscoIeee8021CfmExtCapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmExtCapCatOSV08R0702 = ciscoIeee8021CfmExtCapCatOSV08R0702.setStatus('current')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-EXT-CAPABILITY", ciscoIeee8021CfmExtCapability=ciscoIeee8021CfmExtCapability, PYSNMP_MODULE_ID=ciscoIeee8021CfmExtCapability, ciscoIeee8021CfmExtCapCatOSV08R0702=ciscoIeee8021CfmExtCapCatOSV08R0702)

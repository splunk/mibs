#
# PySNMP MIB module CISCO-SECURE-SHELL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SECURE-SHELL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ciscoSecureShellCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoSecureShellCapability.setRevisions(('2004-04-19 00:00',))
if mibBuilder.loadTexts: ciscoSecureShellCapability.setLastUpdated('200404190000Z')
if mibBuilder.loadTexts: ciscoSecureShellCapability.setOrganization('Cisco Systems, Inc.')
cSecureShellCapCatOSV08R0401k9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setProductRelease('Cisco CatOS 8.4(1) cryptographic\n                         software with Secure Shell support.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setStatus('current')
mibBuilder.exportSymbols("CISCO-SECURE-SHELL-CAPABILITY", ciscoSecureShellCapability=ciscoSecureShellCapability, cSecureShellCapCatOSV08R0401k9=cSecureShellCapCatOSV08R0401k9, PYSNMP_MODULE_ID=ciscoSecureShellCapability)

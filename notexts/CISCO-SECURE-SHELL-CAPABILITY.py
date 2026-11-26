#
# PySNMP MIB module CISCO-SECURE-SHELL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SECURE-SHELL-CAPABILITY
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
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoSecureShellCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoSecureShellCapability.setRevisions(('2004-04-19 00:00',))
if mibBuilder.loadTexts: ciscoSecureShellCapability.setLastUpdated('200404190000Z')
if mibBuilder.loadTexts: ciscoSecureShellCapability.setOrganization('Cisco Systems, Inc.')
cSecureShellCapCatOSV08R0401k9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setProductRelease('Cisco CatOS 8.4(1) cryptographic\n                         software with Secure Shell support.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setStatus('current')
mibBuilder.exportSymbols("CISCO-SECURE-SHELL-CAPABILITY", ciscoSecureShellCapability=ciscoSecureShellCapability, PYSNMP_MODULE_ID=ciscoSecureShellCapability, cSecureShellCapCatOSV08R0401k9=cSecureShellCapCatOSV08R0401k9)

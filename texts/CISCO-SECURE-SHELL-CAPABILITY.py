#
# PySNMP MIB module CISCO-SECURE-SHELL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SECURE-SHELL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoSecureShellCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoSecureShellCapability.setRevisions(('2004-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSecureShellCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSecureShellCapability.setLastUpdated('200404190000Z')
if mibBuilder.loadTexts: ciscoSecureShellCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSecureShellCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSecureShellCapability.setDescription('The capabilities description of\n                CISCO-SECURE-SHELL-MIB.')
cSecureShellCapCatOSV08R0401k9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setProductRelease('Cisco CatOS 8.4(1) cryptographic\n                         software with Secure Shell support.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSecureShellCapCatOSV08R0401k9 = cSecureShellCapCatOSV08R0401k9.setStatus('current')
if mibBuilder.loadTexts: cSecureShellCapCatOSV08R0401k9.setDescription('CISCO-SECURE-SHELL-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SECURE-SHELL-CAPABILITY", ciscoSecureShellCapability=ciscoSecureShellCapability, cSecureShellCapCatOSV08R0401k9=cSecureShellCapCatOSV08R0401k9, PYSNMP_MODULE_ID=ciscoSecureShellCapability)

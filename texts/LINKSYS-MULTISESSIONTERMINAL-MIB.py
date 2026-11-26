#
# PySNMP MIB module LINKSYS-MULTISESSIONTERMINAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-MULTISESSIONTERMINAL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:12:02 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, Gauge32, Unsigned32, NotificationType, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, MibIdentifier, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Gauge32", "Unsigned32", "NotificationType", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "MibIdentifier", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlMultiSessionTerminal = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 69))
rlMultiSessionTerminal.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlMultiSessionTerminal.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlMultiSessionTerminal.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlMultiSessionTerminal.setOrganization('\n                              Linksys LLC.')
if mibBuilder.loadTexts: rlMultiSessionTerminal.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlMultiSessionTerminal.setDescription('This private MIB module defines Multi Session Terminal private MIBs.')
rlTerminalDebugModePassword = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 69, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTerminalDebugModePassword.setStatus('current')
if mibBuilder.loadTexts: rlTerminalDebugModePassword.setDescription('When a user wants to change the terminal mode\n            from debug mode to ASCII he must enter this password first')
mibBuilder.exportSymbols("LINKSYS-MULTISESSIONTERMINAL-MIB", rlMultiSessionTerminal=rlMultiSessionTerminal, PYSNMP_MODULE_ID=rlMultiSessionTerminal, rlTerminalDebugModePassword=rlTerminalDebugModePassword)
